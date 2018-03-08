'''
Database Interface for the application.
V 0.1
'''

from pymongo import MongoClient
from mongoengine import *
import datetime

# This needs to have parameters for imputs
class LPMDB():
    def __init__(self):
        print "Initializing Database..."

    def demodatabse(self):
        print("localhost:27017")
        client = MongoClient('localhost',27017)
        db = client['testing_database']
        post = db.posts
        testingdata = {
            "username" : "testser"
            "password" : "password1!"
        }
        result = post.insert_one(testingdata)
        print('One post: {0}'.format(result.inserted_id)

def main():
    test = LPMDB()
    test.demodatabse()

if __name__ == '__main__':
    main()
