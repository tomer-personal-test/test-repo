"""
Vulnerable test file 356
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 3560
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3560"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3560"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3560"

def render_page_3561(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

