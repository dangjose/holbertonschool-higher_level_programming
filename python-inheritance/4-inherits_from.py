#!/usr/bin/python3
"""Task 4. Only sub class of"""


def inherits_from(obj, a_class):
    """
        Args:
            obj: Object
            a_class: Class to search object

        Returns:
            Boolean
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
