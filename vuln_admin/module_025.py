"""
Vulnerable test file 500
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_5000(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def load_data_5001(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

