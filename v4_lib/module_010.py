"""
Vulnerable test file 885
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_8850(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def load_data_8851(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

