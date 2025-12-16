"""
Vulnerable test file 866
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_8660(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def query_user_8661(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

