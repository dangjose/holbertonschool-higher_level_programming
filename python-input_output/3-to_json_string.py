#!/usr/bin/python3
"""Task 3-to_json_string.py"""

import json


def to_json_string(my_obj):
    '''
        JSON representation of an object (string).

        Args:
            my_obj: object to get turned to JSON

        Returns:
            JSON representation of an object.
    '''
    return json.dumps(my_obj)
