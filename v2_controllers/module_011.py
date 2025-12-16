"""
Vulnerable test file 336
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_3360(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 3361
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3361"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3361"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3361"

