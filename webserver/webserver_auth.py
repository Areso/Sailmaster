#!/usr/bin/env python3
import os
import uuid
import time
import json
import logging
from flask import Flask, jsonify
from flask import request
import mysql.connector


app = Flask(__name__)


def myloading():
    cfgpath = "config_auth.txt"
    fconf = open(cfgpath, 'r')
    tconf = fconf.read()
    fconf.close()
    conf_list = tconf.split('\n')
    return conf_list, len(conf_list)


def opencon(myconfig):
    global mydb
    mydb = mysql.connector.connect(
        host=myconfig[0],
        port=myconfig[1],
        database=myconfig[2],
        user=myconfig[3],
        passwd=myconfig[4]
    )
    global salt
    salt = myconfig[5]
    print("open db connection")


@app.route('/api/v1.0/heartbeat', methods=['GET', 'OPTIONS'])
def heartbeat():
    return "auth webserver is UP", 200, {"Access-Control-Allow-Origin": "*",
                                         "Content-type": "application/json",
                                         "Access-Control-Allow-Methods": "POST"}


@app.route('/api/v1.0/db_heartbeat', methods=['GET', 'OPTIONS'])
def db_heartbeat():
    global mydb
    code = 500
    #TODO check mydb is not {}
    answer = "db server is DOWN"
    try:
        mydb.ping(reconnect=True, attempts=1, delay=0)
        mycursor   = mydb.cursor()
        mycursor.execute('SELECT * FROM dbstat;')
        myresult = mycursor.fetchall()
        if len(myresult) != 0:
            result = myresult[0][0]
            code   = 200
            answer = "db server is UP"
        else:
            code   = 500
            answer = "db server is DOWN"
    except Exception as error:
        code   = 500
        answer = error
    return answer, code, {"Access-Control-Allow-Origin": "*",
                                         "Content-type": "application/json",
                                         "Access-Control-Allow-Methods": "POST"}


@app.route('/api/v1.0/mq_heartbeat', methods=['GET', 'OPTIONS'])
def mq_heartbeat():
    return "mq server is UP", 200, {"Access-Control-Allow-Origin": "*",
                                         "Content-type": "application/json",
                                         "Access-Control-Allow-Methods": "POST"}


@app.route('/api/v1.0/gameserver_heartbeat', methods=['GET', 'OPTIONS'])
def gameserver_heartbeat():
    return "gameserver is UP", 200, {"Access-Control-Allow-Origin": "*",
                                         "Content-type": "application/json",
                                         "Access-Control-Allow-Methods": "POST"}



@app.route('/api/v1.0/account_create', methods=['POST', 'OPTIONS'])
def account_create():
    code       = 200
    stat_msg   = "ok"
    token_uniq = False
    global mydb
    #TODO check that mydb has type of {}. If that, throw 500
    while token_uniq == False:
        token       = uuid.uuid4()
        token       = str(token)
        logger.info("we are here get token "+token)
        wait_length = 0
        time.sleep(wait_length)
        try:
            logger.info("we are inside the try")
            mydb.ping(reconnect=True, attempts=1, delay=0)
            mycursor   = mydb.cursor()
            s_token = str(token)
            mycursor.execute('SELECT id_acc, token FROM accounts WHERE token = %(token)s;', 
                           {'token':token})
            myresult = mycursor.fetchall()
            logger.info("check token")
            wait_length
            if len(myresult) == 0:
                token_uniq = True
        except Exception as error:
            print(error)
            code     = 500
            stat_msg = "couldn't get tokens from the database"
    # create an account with the token
    if token_uniq == True:
        try:
            mydb.ping(reconnect=True, attempts=1, delay=0)
            mycursor   = mydb.cursor()
            mycursor.execute("INSERT INTO accounts(token) VALUES (%(token)s)",
                              {'token':token})
            mydb.commit()
        except:
            if code     != 500:
                code     = 500
                stat_msg = "couldn't insert new account"
        try:
            #TO DO TODO SELECT LAST_INSERT_ID();
            mycursor = mydb.cursor()
            mycursor.execute('SELECT id_acc FROM accounts WHERE token = %(token)s;',
                             {'token': token})
            myresult  = mycursor.fetchall()
            id_acc    = myresult[0][0]
        except:
            if code     != 500:
                code     = 500
                stat_msg = "couldn't read inserted account from the database"
    if token_uniq == False:
        code      = 500
        stat_msg  = "couldn't reserve a new token for a newly created account. acc creation is aborted"
    if code == 200:
        accounts.append({token, id_acc})
    print("creation account stat is "+stat_msg)
    print(accounts)
    return {"status": stat_msg, "token": token}, code, {"Access-Control-Allow-Origin": "*",
                                                        "Content-type": "application/json",
                                                        "Access-Control-Allow-Methods": "POST"}


if __name__ == "__main__":
    mydb     = {}
    accounts = []
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("auth.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("auth server started")
    testing = os.environ.get("sail_testing", False)
    logger.info(testing)
    if testing == False:
        myconfig = myloading()[0]
        opencon(myconfig)
    app.debug = True
    app.run(host='0.0.0.0', port=6689)
