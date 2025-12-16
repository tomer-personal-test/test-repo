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
    # LDAP Injection
    '''def ldap_search_{idx}(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)
''',
    # XML External Entity
    '''def parse_xml_{idx}(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)
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

# Create directory structure (40 directories for 1000 files)
directories = [
    'v1_api', 'v1_auth', 'v1_config', 'v1_controllers', 'v1_helpers',
    'v1_lib', 'v1_models', 'v1_routes', 'v1_services', 'v1_utils',
    'v2_api', 'v2_auth', 'v2_config', 'v2_controllers', 'v2_helpers',
    'v2_lib', 'v2_models', 'v2_routes', 'v2_services', 'v2_utils',
    'v3_workers', 'v3_tasks', 'v3_middleware', 'v3_processors', 'v3_integrations',
    'v3_webhooks', 'v3_scripts', 'v3_validators', 'v3_cron', 'v3_admin',
    'v4_api', 'v4_auth', 'v4_config', 'v4_controllers', 'v4_helpers',
    'v4_lib', 'v4_models', 'v4_routes', 'v4_services', 'v4_utils',
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Generate 1000 files
files_per_dir = 1000 // len(directories)
extra_files = 1000 % len(directories)

file_num = 0
for dir_idx, directory in enumerate(directories):
    num_files = files_per_dir + (1 if dir_idx < extra_files else 0)
    
    for i in range(num_files):
        file_num += 1
        filename = f"{directory}/module_{i+1:03d}.py"
        content = generate_file(file_num)
        
        with open(filename, 'w') as f:
            f.write(content)
        
        if file_num % 100 == 0:
            print(f"Created {file_num} files...")

print(f"\nTotal files created: {file_num}")
print(f"Expected findings: ~{file_num * 1.5:.0f} (1-2 per file)")
