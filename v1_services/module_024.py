"""
Vulnerable test file 224
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_2240(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

