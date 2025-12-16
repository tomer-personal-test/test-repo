"""
Vulnerable test file 371
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_3710(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def render_page_3711(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

