"""
Vulnerable test file 561
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_5610(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 5611
API_KEY = "sk_live_51H7YZ2eZvKYlo2C5611"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz5611"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY5611"

