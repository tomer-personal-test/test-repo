"""
Vulnerable test file 919
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_9190(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_9191(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

