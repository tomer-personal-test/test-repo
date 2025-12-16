"""
Vulnerable test file 434
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4340(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def execute_command_4341(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

