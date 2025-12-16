"""
Vulnerable test file 365
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_3650(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def execute_command_3651(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

