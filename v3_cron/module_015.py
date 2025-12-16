"""
Vulnerable test file 715
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_7150(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def render_page_7151(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

