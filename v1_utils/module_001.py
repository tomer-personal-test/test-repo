"""
Vulnerable test file 226
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2260(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

