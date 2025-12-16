"""
Vulnerable test file 490
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_4900(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def ldap_search_4901(username):
    """LDAP injection vulnerability"""
    filter = "(uid=" + username + ")"
    return ldap.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

