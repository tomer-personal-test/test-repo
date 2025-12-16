"""
Vulnerable test file 761
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_7610(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def find_user_7611(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

