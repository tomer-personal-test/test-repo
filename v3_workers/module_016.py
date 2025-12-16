"""
Vulnerable test file 516
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def render_page_5160(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

def parse_xml_5161(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

