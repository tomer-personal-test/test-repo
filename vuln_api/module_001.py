"""
Vulnerable test file 1
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_10(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

