"""
Vulnerable test file 303
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_3030(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

