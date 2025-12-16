"""
Vulnerable test file 952
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_9520(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def parse_xml_9521(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

