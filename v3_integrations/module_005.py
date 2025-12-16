"""
Vulnerable test file 605
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_6050(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def read_file_6051(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

