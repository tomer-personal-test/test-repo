"""
Vulnerable test file 817
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_8170(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

