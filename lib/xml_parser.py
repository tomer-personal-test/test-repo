import xml.etree.ElementTree as ET
from lxml import etree
import xml.sax

class XMLParser:
    def parse_xml(self, xml_string):
        # XXE vulnerability
        return ET.fromstring(xml_string)
    
    def parse_lxml(self, xml_string):
        # XXE vulnerability
        parser = etree.XMLParser()
        return etree.fromstring(xml_string, parser)
    
    def parse_file(self, filename):
        # XXE vulnerability
        tree = ET.parse(filename)
        return tree.getroot()
