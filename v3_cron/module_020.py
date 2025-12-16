"""
Vulnerable test file 720
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_7200(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def load_data_7201(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

