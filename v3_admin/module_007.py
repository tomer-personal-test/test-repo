"""
Vulnerable test file 732
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_7320(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def find_user_7321(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

