"""
Vulnerable test file 741
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_7410(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# Configuration for service 7411
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7411"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7411"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7411"

