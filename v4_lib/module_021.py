"""
Vulnerable test file 896
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_8960(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def load_data_8961(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

