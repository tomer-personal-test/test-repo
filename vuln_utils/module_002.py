"""
Vulnerable test file 227
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_2270(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def load_data_2271(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

