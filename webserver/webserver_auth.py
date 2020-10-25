#!/usr/bin/env python3
import json
import logging
from flask import Flask, jsonify
from flask import request
import mysql.connector

app = Flask(__name__)

#SYNC
def myloading():
    cfgpath = "config_auth.txt"
    fconf = open(cfgpath, 'r')
    tconf = fconf.read()
    fconf.close()
    conf_list = tconf.split('\n')
    return conf_list


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


if __name__ == "__main__":
    myconfig=myloading()
    opencon(myconfig)
    app.debug = True
    app.run(host='0.0.0.0', port=6689)
