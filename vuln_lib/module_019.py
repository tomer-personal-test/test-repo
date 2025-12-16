"""
Vulnerable test file 144
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_1440(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

