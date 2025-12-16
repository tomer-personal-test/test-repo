"""
Vulnerable test file 218
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2180(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_2181(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

