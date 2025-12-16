"""
Vulnerable test file 212
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_2120(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def ldap_search_2121(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

