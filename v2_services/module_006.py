"""
Vulnerable test file 456
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_4560(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def render_page_4561(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

