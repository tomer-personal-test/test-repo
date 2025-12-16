"""
Vulnerable test file 897
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_8970(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 8971
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8971"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8971"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8971"

