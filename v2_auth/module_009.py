"""
Vulnerable test file 284
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2840(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def execute_command_2841(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

