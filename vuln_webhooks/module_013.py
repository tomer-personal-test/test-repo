"""
Vulnerable test file 388
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 3880
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3880"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3880"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3880"

def render_page_3881(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

