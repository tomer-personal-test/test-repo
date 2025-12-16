"""
Vulnerable test file 35
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 350
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0350"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0350"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0350"

def ldap_search_351(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

