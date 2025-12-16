"""
Vulnerable test file 580
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_5800(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def find_user_5801(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

