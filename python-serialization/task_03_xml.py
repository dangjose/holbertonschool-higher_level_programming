#!/usr/bin/python3
"""Task 3. Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''
        Serialize dictionary into XML and save to file.

        Args:
            dictionary: Dictionary to be serialized.
            filename: Name of file to save to.
    '''

    root = ET.Element('dictionary')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="UTF-8", xml_declaration=True)


def deserialize_from_xml(filename):
    '''
        Deserialize XML data from file.

        Args:
            filename: Name of file to deserialize.

        Return:
            Deserialized python dictionary.
    '''

    tree = ET.parse(filename)
    root = tree.getroot()
    xml_dict = {}

    for child in root:
        xml_dict[child.tag] = child.text

    return xml_dict
