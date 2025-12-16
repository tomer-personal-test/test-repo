"""
Vulnerable test file 169
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1690(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def execute_command_1691(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

