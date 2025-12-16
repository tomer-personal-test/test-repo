"""
Vulnerable test file 495
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_4950(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def find_user_4951(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

