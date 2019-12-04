import urllib.request, json, base64
import os
from datetime import datetime, date, time
from configparser import RawConfigParser
import crypto


# values provided into environment by cumulocity platform during deployment
C8Y_BASEURL = os.getenv('C8Y_BASEURL')
C8Y_BOOTSTRAP_USER = os.getenv('C8Y_BOOTSTRAP_USER')
C8Y_BOOTSTRAP_TENANT = os.getenv('C8Y_BOOTSTRAP_TENANT')
C8Y_BOOTSTRAP_PASSWORD = os.getenv('C8Y_BOOTSTRAP_PASSWORD')

class Credentials(object):

    def __init__(self,\
                 C8Y_BASEURL = os.getenv('C8Y_BASEURL'), \
                 C8Y_BOOTSTRAP_USER = os.getenv('C8Y_BOOTSTRAP_USER'), \
                 C8Y_BOOTSTRAP_TENANT = os.getenv('C8Y_BOOTSTRAP_TENANT'), \
                 C8Y_BOOTSTRAP_PASSWORD = os.getenv('C8Y_BOOTSTRAP_PASSWORD') ):
        self.C8Y_BASEURL = C8Y_BASEURL
        self.C8Y_BOOTSTRAP_USER = C8Y_BOOTSTRAP_USER
        self.C8Y_BOOTSTRAP_TENANT = C8Y_BOOTSTRAP_TENANT
        self.__C8Y_BOOTSTRAP_PASSWORD = C8Y_BOOTSTRAP_PASSWORD

        self.username = username
        self.__password = CryptoHandler.decrypt(password)
