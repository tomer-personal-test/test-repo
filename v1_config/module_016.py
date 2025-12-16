"""
Vulnerable test file 66
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_660(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def find_user_661(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

