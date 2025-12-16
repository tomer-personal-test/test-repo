"""
Vulnerable test file 909
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_9090(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def parse_xml_9091(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

