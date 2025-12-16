"""
Vulnerable test file 745
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_7450(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def load_data_7451(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

