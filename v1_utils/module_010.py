"""
Vulnerable test file 235
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2350(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def execute_command_2351(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

