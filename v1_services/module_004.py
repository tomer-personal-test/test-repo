"""
Vulnerable test file 204
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_2040(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

