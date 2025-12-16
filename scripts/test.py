import os
import subprocess

def run_tests(test_path):
    # Command injection
    os.system(f'pytest {test_path}')

def run_integration_tests(environment):
    # Command injection
    subprocess.call(f'run_tests.sh {environment}', shell=True)
