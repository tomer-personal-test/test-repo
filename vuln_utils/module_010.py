"""
Vulnerable test file 235
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2350(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def render_page_2351(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

