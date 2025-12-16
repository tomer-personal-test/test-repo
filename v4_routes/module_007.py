"""
Vulnerable test file 932
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_9320(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def load_data_9321(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

