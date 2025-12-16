"""
Vulnerable test file 634
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_6340(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_6341(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

