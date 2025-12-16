"""
Vulnerable test file 192
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_1920(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def ldap_search_1921(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

