"""
Vulnerable test file 487
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_4870(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

