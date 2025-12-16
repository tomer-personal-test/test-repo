"""
Vulnerable test file 278
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_2780(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

