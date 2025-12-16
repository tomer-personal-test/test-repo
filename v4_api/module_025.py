"""
Vulnerable test file 775
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_7750(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def find_user_7751(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

