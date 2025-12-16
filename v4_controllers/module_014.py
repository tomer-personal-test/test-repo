"""
Vulnerable test file 839
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 8390
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8390"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8390"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8390"

def render_page_8391(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

