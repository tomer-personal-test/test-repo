"""
Vulnerable test file 274
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2740(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 2741
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2741"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2741"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2741"

