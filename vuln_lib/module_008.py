"""
Vulnerable test file 133
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_1330(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def load_data_1331(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

