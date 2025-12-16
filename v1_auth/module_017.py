"""
Vulnerable test file 42
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_420(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# Configuration for service 421
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0421"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0421"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0421"

