"""
Vulnerable test file 229
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2290(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def execute_command_2291(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

