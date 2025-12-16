"""
Vulnerable test file 659
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 6590
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6590"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6590"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6590"

def parse_xml_6591(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

