#!/usr/bin/python3
"""Task 4. From JSON string to Object"""

import json


def from_json_string(my_str):
    '''
        Object represented by a JSON string

        Args:
            my_str: string to turn to object.

        Returns:
            Object (Python data structure) represented by a JSON string
    '''
    return json.loads(my_str)
