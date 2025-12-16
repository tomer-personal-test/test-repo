"""
Vulnerable test file 328
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_3280(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 3281
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3281"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3281"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3281"

