"""
Vulnerable test file 482
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_4820(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_4821(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

