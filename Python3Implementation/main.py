#!/usr/local/bin/python3

# Imports
import os, sys, logging

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('cllpm.log', mode='a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:[%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

VERSION=0.6

logger.info("Python3 implementation PMAGE v{0}".format(VERSION))



