"""
Vulnerable test file 795
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_7950(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def find_user_7951(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

