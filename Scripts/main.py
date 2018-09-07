#!/usr/bin python

import os
from pgenerator import LPM
from account import Account


accnt = Account()

accnt.name = "SomeAccount"
accnt.password = "12345"
accnt.timestamp = "someday"
accnt.id = "someID"

pwmanager = LPM(name=accnt.name, length=10, symbols=0, password=accnt.password)

print pwmanager.password_funct()
accnt.accountInfo()