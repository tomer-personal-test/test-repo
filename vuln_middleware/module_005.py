"""
Vulnerable test file 305
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_3050(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def render_page_3051(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

