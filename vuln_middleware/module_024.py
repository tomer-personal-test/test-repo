"""
Vulnerable test file 324
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_3240(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def find_user_3241(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

