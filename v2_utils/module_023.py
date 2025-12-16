"""
Vulnerable test file 498
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_4980(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# Configuration for service 4981
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4981"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4981"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4981"

