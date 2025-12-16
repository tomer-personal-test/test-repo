"""
Vulnerable test file 311
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_3110(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def read_file_3111(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

