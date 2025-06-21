#!/usr/bin/python3
"""Task 2. Exact same object"""


def is_same_class(obj, a_class):
    """
        Args:
            obj: Object
            a_class: Class to search object

        Returns:
            Boolean
    """
    return type(obj) == a_class
