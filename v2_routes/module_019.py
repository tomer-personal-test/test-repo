"""
Vulnerable test file 444
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4440(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def ldap_search_4441(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

