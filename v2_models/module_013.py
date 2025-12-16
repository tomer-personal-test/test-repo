"""
Vulnerable test file 413
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_4130(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def render_page_4131(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

