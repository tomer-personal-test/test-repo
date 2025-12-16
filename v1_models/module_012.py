"""
Vulnerable test file 162
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_1620(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 1621
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1621"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1621"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1621"

