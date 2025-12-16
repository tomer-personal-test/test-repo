"""
Vulnerable test file 263
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2630
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2630"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2630"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2630"

def render_page_2631(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

