"""
Vulnerable test file 409
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4090
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4090"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4090"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4090"

def render_page_4091(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

