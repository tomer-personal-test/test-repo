"""
Vulnerable test file 457
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4570
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4570"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4570"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4570"

def parse_xml_4571(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

