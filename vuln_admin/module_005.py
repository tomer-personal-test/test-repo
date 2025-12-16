"""
Vulnerable test file 480
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_4800(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

