'''
Database Interface for Pgenerator
'''



from mongoengine import *
import datetime

class Account(Account):
    uid = UUIDField()
    username = StringField(max_length=20, required=True)
    password = StringField(max_length=20, required=True)

def main():
    test = Account(uid='12dedwe', username='tester', password='testerpassword')

if __name__ == '__main__':
    main()