# !/LPM/bin/python 

VERSION = 0.1
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

Should this have a secret key? 

"""

'imports'
import hashlib
import argparse
import logging
import sys
import os
import sqlite3

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('pgenerator.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(name)s : [%(levelname)s] : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class LPM():
    def __init__(self, name, length, symbols):
        self.name = None
        self.length = 8 #default
        self.symbols = True #does it contain symbols
        self.alphabet = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')
        self.password = None #user password
        
    def get_alphabet(self):
        if self.alphabet:
            return self.alphabet
        alpha = ('abcdefghijklmnopqrstuvwxyz'
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '0123456789')
        if self.symbols:
            alpha += '!@#$%^&*()-_'
        return alpha

    def get_hexdigest(self, salt, plaintext):
        return hashlib.sha256(salt+plaintext)

    def make_password(self, plaintext, service):
        salt = self.get_hexdigest(SECRET_KEY, self.name)
        hsh = self.get_hexdigest(salt, plaintext)
        return ''.join((salt, hsh))

    def password(self):
        #check variables
        raw_hexdigest = self.make_password(plaintext, service)

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
        return password(plaintext, self.name, self.length,
                        self.get_alphabet())

    def create():
        pass


def main_args():
    # Define arguments
    # Have a functional argparser befre begining full code. 
    p = argparse.ArgumentParser(prog='pgenerator.py',
                                description='Generate a strong password',
                                epilog='Author: Ricardo Castro')
    p.add_argument("-t",
                   help="Run a test",action='store_true')
    p.add_argument("-s", type=str,
                   help="Input secret key:  -s [key]")
    p.add_argument("--on", action="store_true",
                   help="include to enable")
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0,
                   help="increase output verbosity")
    

    return(p.parse_args())

if __name__ == '__main__':
    logger.info("Initial testing completed")
    args = main_args()

    if args.t:
        gen = Service(name='amazon',length=10,symbols=True)
        print gen
    else:
        #This is printing some weird thing
        print(main_args())