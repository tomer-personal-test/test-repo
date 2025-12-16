"""
Vulnerable test file 164
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_1640(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def execute_command_1641(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

