"""
Vulnerable test file 475
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4750
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4750"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4750"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4750"

def render_page_4751(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

