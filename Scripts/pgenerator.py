# !/LPM/python 

version = 0.1

"""
Password generator using a concept from this interesting article: 

http://charlesleifer.com/blog/creating-a-personal-password-manager/

basically the article states that a good way to generate passwords is to use the account type
as a salt for a hash and from that you choose a password and generate a password from that.

This makes it harder for the account to be attacked by a password brute force attack or library attack.
"""



