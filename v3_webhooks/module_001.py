"""
Vulnerable test file 626
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_6260(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def execute_command_6261(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

