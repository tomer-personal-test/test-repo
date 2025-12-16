"""
Vulnerable test file 257
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_2570(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def query_user_2571(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

