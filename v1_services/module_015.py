"""
Vulnerable test file 215
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2150
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2150"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2150"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2150"

def ldap_search_2151(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

