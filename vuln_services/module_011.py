"""
Vulnerable test file 211
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_2110(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def load_data_2111(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

