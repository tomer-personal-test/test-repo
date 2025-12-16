import xml.etree.ElementTree as ET

class XMLValidator:
    def validate(self, xml_string):
        try:
            # XXE vulnerability
            ET.fromstring(xml_string)
            return True
        except:
            return False
