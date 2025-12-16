"""
Vulnerable test file 891
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_8910(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def find_user_8911(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

