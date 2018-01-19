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

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('pgenerator.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class generate():
    def __init__(self):
        self.salt = 'salt'
        self.password = 'password'
        # should a password length be required 
        # upper and lower case? 

    def get_hexdigest(self, salt, password):
        return hashlib.sha256(salt+password).hexdigest()

    def create_password(self):
        pass 

def main_args():
    # Define arguments
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
    
    group1 = p.add_mutually_exclusive_group(required=True)
    group1.add_argument('--enable',action="store_true")
    group1.add_argument('--disable',action="store_false")
 
    return(p.parse_args())

if __name__ == '__main__':
    logger.info("Initial testing completed")
    args = main_args()

    print(args)