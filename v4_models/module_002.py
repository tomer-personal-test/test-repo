"""
Vulnerable test file 902
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_9020(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def load_data_9021(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

