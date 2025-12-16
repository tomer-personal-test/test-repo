"""
Vulnerable test file 133
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_1330(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def render_page_1331(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

