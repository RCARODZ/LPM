#!/usr/bin python

class A(object):
    def __init__(self, name, account, length):
        self.name = name
        self.account = account
        self.length = length
    
    def someFunct(self):
        print self.account

class B(A):
    def __init__(self, name, account, length):
        A.__init__(self, name, account, length)

    def display(self):
        print self.name


