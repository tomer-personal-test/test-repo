"""
Vulnerable test file 924
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_9240(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 9241
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9241"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9241"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9241"

