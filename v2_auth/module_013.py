"""
Vulnerable test file 288
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_2880(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_2881(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

