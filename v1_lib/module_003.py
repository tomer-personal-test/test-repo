"""
Vulnerable test file 128
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_1280(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def load_data_1281(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

