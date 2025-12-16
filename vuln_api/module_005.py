"""
Vulnerable test file 5
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_50(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 51
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0051"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0051"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0051"

