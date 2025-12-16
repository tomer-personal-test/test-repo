"""
Vulnerable test file 850
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_8500(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def read_file_8501(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

