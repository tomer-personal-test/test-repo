"""
Vulnerable test file 173
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_1730(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def render_page_1731(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

