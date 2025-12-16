"""
Vulnerable test file 449
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_4490(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def query_user_4491(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

