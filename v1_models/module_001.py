"""
Vulnerable test file 151
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_1510(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 1511
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1511"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1511"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1511"

