"""
Vulnerable test file 392
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_3920(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def render_page_3921(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

