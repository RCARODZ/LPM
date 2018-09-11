# !/usr/bin/python 

VERSION = 1.3
SECRET_KEY = 'secret'

"""
Password generator using a concept from this interesting article: 

http://charlesleifer.com/blog/creating-a-personal-password-manager/

basically the article states that a good way to generate passwords is to use the account type
as a salt for a hash and from that you choose a password and generate a password from that.

This makes it harder for the account to be attacked by a password brute force attack or library attack.

- Define a salt / this could be the account the user is creating the password for.
- The user imputs a password they want
- Generates a password from those parameters
- Verify function generating the password, its always printing the same thing.

Todo:

Create an integration with a database.

Create easy user interaction. (add, remove, modify)

"""

# IMPORTS
import hashlib
import argparse
import logging
import sys
import os
import sqlite3 #is this the database im going to use? 
import json, base64
from account import Account

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('cllpm.log', mode='a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Account(object):
    def __init__(self, name, password, id, timestamp, length):
        logger.info("Initializing Account infomration")
        self.name = name
        self.password = password
        self.id = id
        self.timestamp = timestamp
        self.length = length

    def accountInfo(self):
        accnt = """
            Account Information:\n
            Name:{0}\n
            ID:{1}\n
        """.format(self.name, self.id)
        logger.info(accnt)

class LPM(Account):
    def __init__(self, name, password, id, timestamp, length):
        self.symbols = False #does it contain symbols
        self.alphabet = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')
        #Initialize Accounts Instance 
        Account.__init__(self, name, password, id, timestamp, length)
        
        
        
    def get_alphabet(self):
        logger.info('generating alphabet for password...')
        if self.alphabet:
            return self.alphabet
        alpha = ('abcdefghijklmnopqrstuvwxyz'
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '0123456789')
        if self.symbols:
            alpha += '!@#$%^&*()-_'
        return alpha

    def get_hexdigest(self):
        logger.info('generate hexhash...')
        return hashlib.sha256(SECRET_KEY+self.name+self.password).hexdigest()

    def make_password(self, plaintext, service):
        salt = self.get_hexdigest()
        hsh = self.get_hexdigest()
        return ''.join((salt, hsh))


    def password_funct(self):
        logger.warning('password_funct... this function needs to be verified..')
        #check variables
        #its allways returning the same password...
        raw_hexdigest = self.make_password(self.password, self.name)

        # Convert the hexdigest into decimal
        num = int(raw_hexdigest, 16)

        # What base will we convert `num` into?
        num_chars = len(self.alphabet)

        # Build up the new password one "digit" at a time,
        # up to a certain length
        chars = []
        while len(chars) < self.length:
            num, idx = divmod(num, num_chars)
            chars.append(self.alphabet[idx])

        return ''.join(chars)

    def password_handler(self, plaintext):
        return self.password_funct()

class DataBase(LPM):
    def __init___(self,name, password, id, timestamp, length):
        LPM.__init__(self, name, password, id, timestamp, length)
        logger.info("Initializing json database")
        self.fileName = "tester.json"

    def addtoFile(self):
        '''
        This function should appendto the same user multiple accounts that the user inputs
            DemoUser: 
                name: [account]
                ...

                name: [account]
                ...
        '''
        logger.info("Adding data to file")
        json_data = {}
        json_data['DemoUser'] = []
        json_data['DemoUser'].append({
                "ID": str(self.id),
                "name": self.name,
                "password": self.password,
                "Timestamp": self.timestamp,
                "Length": self.length,
                "Genedated": self.password_funct()
        })
        data = json.dumps(json_data, indent=4)
        with open("tester.json", 'a') as jsondata:
            json.dump(data, jsondata)
        logger.warning("This is creating multiple users of the same user... needs fixing")

    def readfromFile(self):
        with open("tester.json", "r") as read_file:
            data = json.load(read_file)

    def removefromFile(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass