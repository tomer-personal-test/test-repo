"""
Vulnerable test file 867
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_8670(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def parse_xml_8671(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

