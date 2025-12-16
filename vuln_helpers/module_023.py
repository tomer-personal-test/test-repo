"""
Vulnerable test file 123
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1230(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def render_page_1231(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

