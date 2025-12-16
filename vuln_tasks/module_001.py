"""
Vulnerable test file 276
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_2760(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def query_user_2761(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

