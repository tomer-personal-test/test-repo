"""
Vulnerable test file 571
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_5710(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def find_user_5711(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

