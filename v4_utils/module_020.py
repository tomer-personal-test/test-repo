"""
Vulnerable test file 995
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_9950(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_9951(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

