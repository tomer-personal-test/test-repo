"""
Vulnerable test file 420
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_4200(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def execute_command_4201(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

