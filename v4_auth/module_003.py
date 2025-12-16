"""
Vulnerable test file 778
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_7780(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def render_page_7781(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

