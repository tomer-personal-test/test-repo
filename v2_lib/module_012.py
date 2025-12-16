"""
Vulnerable test file 387
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_3870(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def ldap_search_3871(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

