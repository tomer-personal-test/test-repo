#!/usr/bin/env python3
import os
import random

# Vulnerability templates with secrets that gitleaks can detect
VULN_TEMPLATES = [
    # SQL Injection
    '''def query_user_{idx}(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)
''',
    # Hardcoded secrets
    '''# Configuration for service {idx}
API_KEY = "sk_live_51H7YZ2eZvKYlo2C{idx:04d}"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz{idx:04d}"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY{idx:04d}"
''',
    # Command Injection
    '''def execute_command_{idx}(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)
''',
    # XSS
    '''def render_page_{idx}(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html
''',
    # Path Traversal
    '''def read_file_{idx}(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()
''',
    # Insecure Deserialization
    '''def load_data_{idx}(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)
''',
    # Weak Crypto
    '''def encrypt_{idx}(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)
''',
    # NoSQL Injection
    '''def find_user_{idx}(username):
    """NoSQL injection vulnerability"""
    query = {{"username": username}}
    return db.users.find(query)
''',
]

def generate_file(file_num):
    """Generate a vulnerable Python file"""
    # Each file will have 1-2 vulnerabilities
    num_vulns = random.randint(1, 2)
    content = f'''"""
Vulnerable test file {file_num}
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

'''
    
    for i in range(num_vulns):
        template = random.choice(VULN_TEMPLATES)
        content += template.format(idx=file_num * 10 + i) + "\n"
    
    return content

# Create directory structure
directories = [
    'vuln_api', 'vuln_auth', 'vuln_config', 'vuln_controllers', 
    'vuln_helpers', 'vuln_lib', 'vuln_models', 'vuln_routes',
    'vuln_services', 'vuln_utils', 'vuln_workers', 'vuln_tasks',
    'vuln_middleware', 'vuln_processors', 'vuln_integrations',
    'vuln_webhooks', 'vuln_scripts', 'vuln_validators', 'vuln_cron',
    'vuln_admin'
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Generate 500 files
files_per_dir = 500 // len(directories)
extra_files = 500 % len(directories)

file_num = 0
for dir_idx, directory in enumerate(directories):
    num_files = files_per_dir + (1 if dir_idx < extra_files else 0)
    
    for i in range(num_files):
        file_num += 1
        filename = f"{directory}/module_{i+1:03d}.py"
        content = generate_file(file_num)
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"Created {filename}")

print(f"\nTotal files created: {file_num}")
print(f"Expected findings: ~{file_num * 1.5:.0f} (1-2 per file)")
