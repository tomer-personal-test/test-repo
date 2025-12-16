"""
Vulnerable test file 13
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_130(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def ldap_search_131(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

