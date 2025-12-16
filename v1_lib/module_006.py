"""
Vulnerable test file 131
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1310
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1310"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1310"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1310"

def render_page_1311(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

