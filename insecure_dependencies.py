# Insecure and outdated dependencies
# requirements.txt would contain:

import flask  # Assuming old version with vulnerabilities
import django  # Assuming old version
import requests  # Assuming old version
import urllib3  # Assuming old version
import pyyaml  # Assuming old version with unsafe load
import jinja2  # Assuming old version
import werkzeug  # Assuming old version

# Using deprecated/insecure functions
import yaml

def load_config(filename):
    with open(filename) as f:
        # Vulnerable: yaml.load without Loader
        return yaml.load(f)

def load_unsafe(data):
    # Vulnerable: unsafe_load
    return yaml.unsafe_load(data)

# Using eval
def calculate(expression):
    # Vulnerable: eval with user input
    return eval(expression)

# Using exec
def run_code(code):
    # Vulnerable: exec with user input
    exec(code)

# Using compile
def compile_code(source):
    # Vulnerable: compile with user input
    return compile(source, '<string>', 'exec')
