"""
Vulnerable test file 210
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2100(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_2101(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

