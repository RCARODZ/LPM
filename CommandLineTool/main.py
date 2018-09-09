import LPM
import logging
import argparse

VERSION = 0

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('cllpm.log', mode='a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def main_args():
    # Define arguments
    # Have a functional argparser befre begining full code. 
    p = argparse.ArgumentParser(prog='main.py',
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

def main():
    print """Welcome to Local Password Manager Command Line Tool V{0}
        -Store Account Passwords Localy
        -Includes a Password Generator to use for creating strong passwords
        
        This tool is developed by Ricardo Castro and it is completley open source.\n""".format(VERSION)

if __name__ == '__main__':
    main()
    
    args = main_args()

    if args.t:
        logger.info("Entered testing evironment...")
        acc = LPM.account.Account()
        acc.name='Home Network'
        acc.length=10
        acc.password="hola"
        lpm = LPM.pgenerator.LPM()
        logger.info('testing parameters:amazon:8:False:another',)
        generated = lpm.password_funct()
        logger.info('password generated:%s [this will only be printed in the test environment]',generated)
        print generated
