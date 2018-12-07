from distutils.core import setup
import logging

from setuptools.command.install import install
import LPM

'''
This command will run when you run setup.py install

TODO: 
    + If .db file does not exist, create one.
    + Will the name be hardcoded?
    + Add this setup into LPM to create an initial setup...
'''

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
logger.info("Using {0} database on setup.py.".format(DB_NAME))

class PostInstallCommand(install):
    """
    Creating setup.py install command
    """
    def run(self):
        """ This runs at install
        Database Setup
        --------------
        - Create Database Instance
        - create_connection(database_name)
        - create_table(query)
        """
        create_table = """ CREATE TABLE IF NOT EXISTS lpm (
            id integer PRIMARY KEY,
            name text NOT NULL,
            date_created text NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            symbols BOOLEAN,
            length INT  ); """
        
        db = LPM.pgenerator.Database()
        db.create_connection(DB_NAME)
        db.create_table(create_table)

        logger.info("Running setup.py install...")
        install.run(self)

REQUIERED = {
    #Required packages for LPM
}

setup(
    name='PASSmage',
    version='0.6dev',
    license='MIT License',
    long_description=open('../README.md').read(),
    author='Ricardo Castro',
    cmdclass={
        'install':PostInstallCommand,
    },
    classifiers=[
        "Programming Languages :: Python :: 2.7",
    ],
)