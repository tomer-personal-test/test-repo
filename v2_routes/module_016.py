"""
Vulnerable test file 441
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_4410(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

