"""
Vulnerable test file 664
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_6640(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def read_file_6641(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

