"""
Vulnerable test file 827
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_8270(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def parse_xml_8271(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

