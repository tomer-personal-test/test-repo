"""
Vulnerable test file 511
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_5110(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# Configuration for service 5111
API_KEY = "sk_live_51H7YZ2eZvKYlo2C5111"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz5111"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY5111"

