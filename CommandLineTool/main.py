import LPM
import logging
import argparse
import time
import uuid
import getpass

VERSION = 0.4

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
    p = argparse.ArgumentParser(prog='main.py',
                                description='Local Password Manager, store passwords, create passwords all from your own machine.',
                                epilog='Author: Ricardo Castro | Pgen V{0}'.format(VERSION))
    p.add_argument("-t",
                   help="Run a test",action='store_true')
    p.add_argument("-s", type=str,
                   help="Input secret key:  -s [key]")
    p.add_argument("-p","--password", help="will prompt you to type a password", action='store_true')
    p.add_argument("-a", "--account", type=str, help="enter account to be used -a [account]")
    p.add_argument("-c","--symbols", type=bool, help="Does the password needs to contain symbol?")
    p.add_argument("--on", action="store_true", help="include to enable")
    p.add_argument("-l", "--length", type=int, help="Length of the password")
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0,
                   help="increase output verbosity")
    # Testing flags
    p.add_argument("-d", "--database", help="run database test", action='store_true')

    return(p.parse_args())

def main():
    print """Welcome to Local Password Manager Command Line Tool V {0}
        -Store Account Passwords Localy
        -Includes a Password Generator to use for creating strong passwords
        
        This tool is developed by Ricardo Castro and it is completelyy open source.\n
        
        -----------------------------------------------------------------------------""".format(VERSION)

def mainPrint(name, password, id, time, length, generated):
    print """
    Output

    Name Input : {0}
    Password Input : {1}
    id : {2}
    Timestamp : {3}
    Length : {4}
    Generated : {5}
    """.format(name, password, id, time, length, generated)

if __name__ == '__main__':
    main()
    timestamp = time.strftime("%d%m%Y", time.gmtime())

    args = main_args()

    if args.t:
        logger.info("Entered testing evironment...")
        lpm = LPM.pgenerator.LPM(name="Amazon", password="somepassword", id=uuid.uuid1(), timestamp=timestamp, length=10)
        logger.info("Sending name={0}, password={1}, id={2}, \
        timestamp={3}, length={4}".format(lpm.name,lpm.password,lpm.id,lpm.timestamp,lpm.length))
        generated = lpm.password_funct()
        logger.info('password generated:%s [this will only be printed in the test environment]',generated)
        mainPrint(lpm.name,lpm.password,lpm.id,lpm.timestamp,lpm.length, lpm.password_funct())
   
    if args.account and args.password and not args.length:
        logger.info("User imput : name and password. Assuming length as 10")
        pwd = getpass.getpass()
        generator = LPM.pgenerator.LPM(name=args.account, password=pwd, 
            id=uuid.uuid1(), timestamp=timestamp, length=10)

        mainPrint(generator.name, "", generator.id, generator.timestamp, 
            generator.length, generator.password_funct())
        
    if args.account and args.password and args.length:
        logger.info("User input : name, password and length")
        pwd = getpass.getpass()
        generator = LPM.pgenerator.LPM(name=args.account, password=pwd,
            id=uuid.uuid1(), timestamp=timestamp, length=args.length)
        
        mainPrint(generator.name, "", generator.id, generator.timestamp, 
            generator.length, generator.password_funct())
        
    if args.password and not args.account:
        logger.info("Only generating a password. Asking user for password")
        #Give user input about password entry, and double check password entry
        pwd = getpass.getpass()
        #Generate a random string for the name
        generator = LPM.pgenerator.LPM("none", pwd, uuid.uuid1(), timestamp, 10)
        print """
            Password Generator: {0}
        """.format(generator.password_funct())
    
    if args.database:
        logger.info("Testing database environment")
        
        #Tester
        lpm = LPM.pgenerator.LPM(name="Amazon", password="somepassword", id=uuid.uuid1(), timestamp=timestamp, length=10)
        logger.info("Sending name={0}, password={1}, id={2}, \
        timestamp={3}, length={4}".format(lpm.name,lpm.password,lpm.id,lpm.timestamp,lpm.length))
        generated = lpm.password_funct()
        databse = LPM.pgenerator.DataBase(name="Amazon", password="somepassword", id=uuid.uuid1(), timestamp=timestamp, length=10)
        databse.addtoFile()
        logger.info('password generated:%s [this will only be printed in the test environment]',generated)
