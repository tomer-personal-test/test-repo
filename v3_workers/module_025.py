"""
Vulnerable test file 525
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_5250(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def ldap_search_5251(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

