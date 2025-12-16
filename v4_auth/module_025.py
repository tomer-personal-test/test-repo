"""
Vulnerable test file 800
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_8000(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def load_data_8001(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

