"""
Vulnerable test file 700
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_7000(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_7001(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

