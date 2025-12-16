"""
Vulnerable test file 384
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_3840(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def render_page_3841(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

