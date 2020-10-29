#!/usr/bin/env python3
import uuid
#import time
import json
import logging
from flask import Flask, jsonify
from flask import request
import mysql.connector

app      = Flask(__name__)

def add(x, y):
    return x + y
def is_positive(x):
    return x > 0

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


@app.route('/api/v1.0/account_create', methods=['POST', 'OPTIONS'])
def createAcc():
    code       = 200
    stat_msg   = "ok"
    token_uniq = False
    # check whether the token is uniq in the database
    global mydb
    while token_uniq == False:
        token      = uuid.uuid4()
        token      = str(token)
        try:
            mydb.ping(reconnect=True, attempts=1, delay=0)
            mycursor   = mydb.cursor()
            s_token = str(token)
            mycursor.execute('SELECT id_acc, token FROM accounts WHERE token = %(token)s;', 
                           {'token':token})
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                token_uniq = True
        except:
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
    myconfig = myloading()[0]
    opencon(myconfig)
    app.debug = True
    app.run(host='0.0.0.0', port=6689)
