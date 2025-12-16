"""
Vulnerable test file 934
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_9340(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 9341
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9341"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9341"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9341"

