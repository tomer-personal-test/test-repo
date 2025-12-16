"""
Vulnerable test file 203
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2030(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_2031(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

