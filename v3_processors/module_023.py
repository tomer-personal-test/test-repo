"""
Vulnerable test file 598
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_5980(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def load_data_5981(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

