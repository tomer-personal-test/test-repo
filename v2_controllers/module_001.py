"""
Vulnerable test file 326
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_3260(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

