"""
Vulnerable test file 990
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_9900(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

