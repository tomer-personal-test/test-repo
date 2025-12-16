"""
Vulnerable test file 465
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_4650(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def find_user_4651(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

