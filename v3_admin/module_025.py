"""
Vulnerable test file 750
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_7500(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

