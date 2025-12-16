"""
Vulnerable test file 77
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_770(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

# Configuration for service 771
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0771"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0771"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0771"

