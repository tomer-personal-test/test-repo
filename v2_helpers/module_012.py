"""
Vulnerable test file 362
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_3620(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def render_page_3621(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

