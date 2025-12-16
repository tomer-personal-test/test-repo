"""
Vulnerable test file 47
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_470(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

# Configuration for service 471
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0471"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0471"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0471"

