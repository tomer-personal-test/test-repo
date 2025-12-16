"""
Vulnerable test file 755
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_7550(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def find_user_7551(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

