"""
Vulnerable test file 749
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_7490(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_7491(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

