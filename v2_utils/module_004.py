"""
Vulnerable test file 479
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_4790(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def find_user_4791(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

