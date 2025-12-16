"""
Vulnerable test file 91
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_910(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def read_file_911(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

