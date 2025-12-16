"""
Vulnerable test file 119
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_1190(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_1191(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

