"""
Vulnerable test file 723
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_7230(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def load_data_7231(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

