"""
Vulnerable test file 411
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4110(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def find_user_4111(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

