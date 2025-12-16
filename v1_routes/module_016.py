"""
Vulnerable test file 191
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_1910(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def query_user_1911(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

