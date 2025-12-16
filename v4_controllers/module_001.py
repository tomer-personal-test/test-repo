"""
Vulnerable test file 826
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_8260(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def ldap_search_8261(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

