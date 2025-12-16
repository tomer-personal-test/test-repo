"""
Vulnerable test file 149
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_1490(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def parse_xml_1491(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

