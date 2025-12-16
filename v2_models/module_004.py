"""
Vulnerable test file 404
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4040
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4040"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4040"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4040"

def render_page_4041(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

