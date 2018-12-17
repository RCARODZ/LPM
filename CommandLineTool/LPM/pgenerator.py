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
import hashlib, argparse, logging, sys, os
import sqlite3 #is this the database im going to use? 
import json, base64
from account import Account
# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
from json import dumps

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('cllpm.log', mode='a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Database
DB_NAME = "actual.db"
logger.info("Using {0} database in pgenerator.py.".format(DB_NAME))

class Database(object):
    """
    This class is used to manage database connections.

    Parameters
    ----------
    conn : sqlite object 
        Creates a connection to a database
    """
    def __init__(self):
        logger.info("Initializing Database.")
        #LPM.__init__(self, name, password, id, timestamp, length)
        self.conn = sqlite3.connect(DB_NAME)

   
    def create_table(self, create_table_sql):
        """ Creates a Table

        Parameters
        ----------
        create_table_sql: str
            A string witht the query for creating the table.

        """
        logger.info("Creating table in database.")
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            logger.error("Database error {0}".format(e))
            print(e)

    def create_connection(self, db_file):
        """ Create a connection to the Database

        Parameters
        ----------
        db_file: str
            Database name

        Returns
        -------
        On success this function returns a connection object of the database.
        On failure this function returns None.
        """
        logger.info("Connecting to database.")
        try:
            self.conn = sqlite3.connect(db_file)
            return self.conn
        except sqlite3.Error as e:
            logger.error("Database connection error {0}".format(e))
            print(e)
        return None


class Account(object):
    """
    Sotres account information

    Parameters
    ----------
    name: str
        username for the account
    password: str
        password for the account
    id: str
        id generated for the account
    timestamp: timestamp
        timestamp generated when the password was created
    length: int
        lenth of the password

    """
    def __init__(self, name, password, id, timestamp, length):
        logger.info("Initializing Account infomration")
        self.name = name
        self.password = password
        self.id = id
        self.timestamp = timestamp
        self.length = length

    def accountInfo(self):
        """ Display account information
        """
        accnt = """
            Account Information:\n
            Name:{0}\n
            ID:{1}\n
        """.format(self.name, self.id)
        logger.info(accnt)

class LPM(Account):
    """
    LPM Account 

    Parameters
    ----------
    symbosl: bool
        Does the user want the password to contain symbols?
    alphabet: dict
        to be used to generate a password
    """
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

