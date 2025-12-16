"""
Vulnerable test file 242
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2420(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

