"""
Vulnerable test file 56
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_560(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def find_user_561(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

