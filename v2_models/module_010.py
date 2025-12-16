"""
Vulnerable test file 410
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_4100(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def load_data_4101(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

