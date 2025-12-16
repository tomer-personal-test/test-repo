"""
Vulnerable test file 338
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_3380(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def render_page_3381(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

