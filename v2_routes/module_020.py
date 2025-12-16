"""
Vulnerable test file 445
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_4450(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def execute_command_4451(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

