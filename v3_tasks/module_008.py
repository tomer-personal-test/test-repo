"""
Vulnerable test file 533
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_5330(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def query_user_5331(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

