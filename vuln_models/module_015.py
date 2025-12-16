"""
Vulnerable test file 165
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_1650(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def execute_command_1651(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

