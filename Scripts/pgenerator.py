# !/LPM/bin/python 

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
import sqlite3

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('pgenerator.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class LPM():
    def __init__(self, name, length, symbols, password):
        self.name = name
        self.length = length #default
        self.symbols = symbols #does it contain symbols
        self.alphabet = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')
        self.password = password #user password
        
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


def main_args():
    # Define arguments
    # Have a functional argparser befre begining full code. 
    p = argparse.ArgumentParser(prog='pgenerator.py',
                                description='Generate a strong password',
                                epilog='Author: Ricardo Castro | Pgen V{0}'.format(VERSION))
    p.add_argument("-t",
                   help="Run a test",action='store_true')
    p.add_argument("-s", type=str,
                   help="Input secret key:  -s [key]")
    p.add_argument("-p","--password", type=str, help="define password -p [password]")
    p.add_argument("-a", "--account", type=str, help="enter account to be used -a [account]")
    p.add_argument("-c","--symbols", type=bool, help="Does the password needs to contain symbol?")
    p.add_argument("--on", action="store_true", help="include to enable")
    p.add_argument("-l", "--length", type=int, help="Length of the password")
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0,
                   help="increase output verbosity")

    return(p.parse_args())

if __name__ == '__main__':
    
    args = main_args()

    #Input variables 
    name = 'Facebook'
    length = 8 #default
    symbols = True
    password = 'password'

    if args.t:
        logger.info("Entered testing evironment...")
        lpm = LPM(name='Home Network', length=10, symbols=False, password='hola')
        logger.info('testing parameters:amazon:8:False:another',)
        generated = lpm.password_funct()
        logger.info('password generated:%s [this will only be printed in the test environment]',generated)
        print generated

    if args.password and args.account and args.length:
        #logger.info('user entered a password:%s',args.password)
        password = args.password
        lpm = LPM(name=args.account, length=args.length, symbols=False, password=args.password)
        logger.info('user entered an account:%s, password:%s, and length:%d', args.account, args.password, args.length)
        passwordgen = lpm.password_funct()
        print passwordgen
    if args.password and args.account:
        logger.info('user entered an account:%s, and password:%s',args.account, args.password)
        name = args.account
        print name
    if args.length:
        logger.info('user entered length for the password:%d',args.length)
        length = args.length
        print length
    if args.symbols:
        logger.info('user answered symbol question')
        symbols = args.symbols
        print symbols

    elif len(sys.argv) == 0: #Something is wrong here
        #This is printing some weird thing
        print(main_args())