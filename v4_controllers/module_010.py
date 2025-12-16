"""
Vulnerable test file 835
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_8350(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

