"""
Vulnerable test file 701
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_7010(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# Configuration for service 7011
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7011"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7011"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7011"

