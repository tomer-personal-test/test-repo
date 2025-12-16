"""
Vulnerable test file 295
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2950(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def parse_xml_2951(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

