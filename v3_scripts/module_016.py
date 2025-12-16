"""
Vulnerable test file 666
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_6660(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def find_user_6661(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

