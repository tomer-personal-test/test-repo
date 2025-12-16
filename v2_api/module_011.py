"""
Vulnerable test file 261
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_2610(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 2611
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2611"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2611"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2611"

