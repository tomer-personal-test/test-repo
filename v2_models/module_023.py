"""
Vulnerable test file 423
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_4230(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_4231(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

