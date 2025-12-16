"""
Vulnerable test file 793
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_7930(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def parse_xml_7931(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

