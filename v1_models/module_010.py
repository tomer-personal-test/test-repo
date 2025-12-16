"""
Vulnerable test file 160
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1600
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1600"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1600"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1600"

def render_page_1601(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

