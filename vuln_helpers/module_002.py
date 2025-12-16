"""
Vulnerable test file 102
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_1020(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_1021(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

