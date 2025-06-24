#!/usr/bin/python3
"""Task 6. Create object from a JSON file"""

import json


def load_from_json_file(filename):
    '''
        Creates an Object from a “JSON file”

        Args:
            filename: JSON file.

        Returns:
            Nothing
    '''
    with open(filename, 'r') as f:
        return json.load(f)
