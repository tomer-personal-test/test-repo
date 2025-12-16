"""
Vulnerable test file 214
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2140(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 2141
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2141"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2141"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2141"

