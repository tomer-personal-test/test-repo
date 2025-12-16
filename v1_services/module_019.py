"""
Vulnerable test file 219
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2190(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_2191(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

