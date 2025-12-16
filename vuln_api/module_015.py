"""
Vulnerable test file 15
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_150(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

