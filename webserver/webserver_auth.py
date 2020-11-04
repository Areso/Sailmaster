#!/usr/bin/env python3
import os
import uuid
import time
import json
import logging
from flask import Flask, jsonify
from flask import request
import mysql.connector
import pika


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


def find_tuple(tuples, value):
    for tup in tuples:
        num, lst = tup
        if value in lst:
            return tup
    return None


class MyMQ:
    """My MQ is a class for creating a pool for MQ server, has add_queue, publish methods"""
    def __init__(self, mq_server, mq_port, mq_user, mq_pass):
        self.mq_server   = mq_server
        self.mq_port     = mq_port
        self.mq_user     = mq_user
        self.mq_pass     = mq_pass
        self.queues      = []
        self.credentials = pika.PlainCredentials(mq_user, mq_pass)
        self.connection  = pika.BlockingConnection(pika.ConnectionParameters(mq_server,
                                                                        mq_port,
                                                                        '/',
                                                                        self.credentials))
        self.channel = self.connection.channel()
    def add_queue(self, exchange, queue):
        self.queues.append([exchange, queue])
        #callback_function = 'callback_'+str(queue)
        #print(callback_function)
        #self.channel.basic_consume(queue=queue, on_message_callback=callback_test, auto_ack=True)
        #self.channel.start_consuming()
    def publish(self, queue, message):
        print(queue)
        the_pair = find_tuple(self.queues, queue)
        print("the pair is ")
        print(the_pair)
        self.channel.queue_declare(queue=the_pair[1])
        self.channel.basic_publish(exchange=the_pair[0],
                                   routing_key=the_pair[1],
                                   body=message)
    def read(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            #print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return body
        else:
            #print('No message returned')
            return 1
    def __del__(self):
        self.connection.close()


def callback_test(ch, method, properties, body):
    #
    print("body of message outside class")
    print(body)
    return 0


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
    global testing
    if not testing:
        mq_obj = MyMQ('localhost',5672,'guest','guest')
        mq_obj.add_queue('','test')
        mq_obj.publish('test', 'test message')
        a = mq_obj.read('test')
        print("mq response is ")
        print(a)
        print(type(a))
        if a.decode('UTF-8')=='test message':
            code   = 200
            answer = "mq server is UP"
        else:
            code   = 500
            answer = "mq server is DOWN"
    else:
        code   = 500
        answer = "mq server is DOWN due to testing env" 
    return answer, code, {"Access-Control-Allow-Origin": "*",
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
    global testing
    testing = os.environ.get("sail_testing", False)
    logger.info(testing)
    if testing == False:
        myconfig = myloading()[0]
        opencon(myconfig)
    app.debug = True
    app.run(host='0.0.0.0', port=6689)
