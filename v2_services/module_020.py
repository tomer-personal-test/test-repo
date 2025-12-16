"""
Vulnerable test file 470
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def parse_xml_4700(xml_data):
    """XXE vulnerability"""
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

def encrypt_4701(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

