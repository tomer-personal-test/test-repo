"""
Vulnerable test file 317
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_3170(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def query_user_3171(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

