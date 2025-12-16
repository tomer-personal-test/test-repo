"""
Vulnerable test file 572
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_5720(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def load_data_5721(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

