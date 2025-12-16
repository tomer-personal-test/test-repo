"""
Vulnerable test file 558
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_5580(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

