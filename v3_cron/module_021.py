"""
Vulnerable test file 721
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_7210(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def parse_xml_7211(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

