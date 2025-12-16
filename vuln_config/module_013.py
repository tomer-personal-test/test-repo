"""
Vulnerable test file 63
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_630(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

