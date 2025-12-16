"""
Vulnerable test file 450
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_4500(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

