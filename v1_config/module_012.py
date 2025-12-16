"""
Vulnerable test file 62
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_620(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def execute_command_621(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

