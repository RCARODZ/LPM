#!/usr/bin python

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('cllpm.log', mode='a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Account(object):
    def __init__(self):
        self.name = ""
        self.password = ""
        self.id = ""
        self.timestamp = ""
        self.length = 0
    
    # Run on debug mode
    def getName(self):
        logger.info(self.name)

    def getID(self):
        logger.info(self.id)

    def accountInfo(self):
        accnt = """
            Account Information:\n
            Name:{0}\n
            ID:{1}\n
        """.format(self.name, self.id)
        logger.info(accnt)