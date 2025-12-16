"""
Vulnerable test file 27
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_270(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# Configuration for service 271
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0271"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0271"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0271"

