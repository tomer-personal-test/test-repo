"""
Vulnerable test file 624
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_6240(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 6241
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6241"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6241"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6241"

