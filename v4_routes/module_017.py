"""
Vulnerable test file 942
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_9420(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

