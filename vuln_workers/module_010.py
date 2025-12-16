"""
Vulnerable test file 260
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_2600(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_2601(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

