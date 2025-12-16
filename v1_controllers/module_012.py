"""
Vulnerable test file 87
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def ldap_search_870(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def render_page_871(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

