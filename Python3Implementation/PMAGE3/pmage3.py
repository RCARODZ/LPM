# Imports
import logging, uuid, hashlib

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('cllpm.log', mode='a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

VERSION = 0.1
SECRET_KEY = "secret"

class Account(object):
    """
    This class implements an account, what is an account? Amazon, Google, etc.

    Parameters
    ----------
    username:   str
        Username for the account, can be an email.

    password:   str
        Password for the account.
    
    name:       str
        Account name

    """
    def __init__(self, name, username, password):
        "Constructor"
        self.username = username
        self.password = password
        self.name = name

    def __account_info(self):
        """
        Print account information method.

        Parameters
        ----------
        None
        """
        logger.info("Printing account information [Name:{0},User:{1},Pass:{2}]".format\
        (self.name, self.username, self.password))
        print("\nAccount Information: \
            \nName: {0}\nUsername: {1}\nPassword {2}".format(self.name, self.username, self.password))

class PMAGE3(Account):
    """
    This class generates passwords using the information from the account. This class inherits from Account.

    Parameters
    ----------
    username:   str
        username from account

    password:   str
        password from account

    length:     int
        desired length of the password (10 default)

    symbols:    boolean
        Variable that determines tif the password should contain symbols.
    id:         str
        Unique ID for the account linking it to the password. Probably to be used
        later in a database implementation.

    timestamp:  timestamp
        Timestamp to know when the passqord was created
    """
    def __init__(self):
        self.id = uuid.uuid3()
        self.symbol = False

        def __get_alphabet(self):
            """
            Chooses between alphabets.

            Parameters
            ----------
            None

            Return:
            Alphabet value
            """
            alpha = ('abcdefghijklmnopqrstuvwxyz'
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '0123456789')
            if self.symbols:
                alpha += '!@#$%^&*()-_'
            return alpha

        def get_hex_digest(self):
            """
            Generate a hash using a key.

            Parameters
            ----------
            None

            Return:
            Generated hash
            """
            key = hashlib.sha256(SECRET_KEY+self.name+self.password).hexdigest()
            logger.info('[__get_hex_digest]:{0}'.format(key))
            return key

        def make_password(self):
            """

            """
            salt = self.get_hex_digest()
            hsh = self.get_hex_digest()
            return ''.join((salt, hsh))

    if __name__ == "__main__":
        print("PMAGE3 v{0}\n".format(VERSION))
        name = input("Enter Name:")
        user = input("Enter User:")
        passw = input("Enter Password:")
        acc = Account(name=name,username=user, password=passw)
        

