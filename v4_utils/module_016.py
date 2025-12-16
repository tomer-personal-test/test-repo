"""
Vulnerable test file 991
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_9910(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def query_user_9911(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

