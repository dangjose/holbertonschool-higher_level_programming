#!/usr/bin/python3
"""Task 8. Class to JSON"""


def class_to_json(obj):
    '''
        Returns the dictionary description of an object
        for JSON serialization.

        Args:
            obj: An instance of a class

        Returns:
            A dictionary of serializable attributes
    '''
    return obj.__dict__
