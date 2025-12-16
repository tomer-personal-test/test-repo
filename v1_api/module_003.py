"""
Vulnerable test file 3
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_30(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def parse_xml_31(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

