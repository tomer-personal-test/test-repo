"""
Vulnerable test file 472
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4720
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4720"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4720"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4720"

def render_page_4721(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

