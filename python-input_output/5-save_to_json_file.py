#!/usr/bin/python3
"""Task 5. Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    '''
        Writes an Object to a text file, using a JSON representation

        Args:
            my_obj: Object to be written.
            filename: file to write to.

        Returns:
            Nothing
    '''
    with open(filename, 'w') as f:
        json.load(my_obj)
