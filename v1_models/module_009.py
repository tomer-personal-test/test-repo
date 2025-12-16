"""
Vulnerable test file 159
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_1590(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def render_page_1591(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

