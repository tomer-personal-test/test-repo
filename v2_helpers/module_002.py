"""
Vulnerable test file 352
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_3520(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 3521
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3521"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3521"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3521"

