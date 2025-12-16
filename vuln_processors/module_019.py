"""
Vulnerable test file 344
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_3440(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

