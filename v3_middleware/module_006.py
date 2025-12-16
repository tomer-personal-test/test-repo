"""
Vulnerable test file 556
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_5560(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_5561(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

