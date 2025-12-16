"""
Vulnerable test file 339
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_3390(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def render_page_3391(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

