"""
Vulnerable test file 41
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 410
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0410"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0410"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0410"

def ldap_search_411(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

