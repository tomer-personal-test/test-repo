"""
Vulnerable test file 22
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_220(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def find_user_221(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

