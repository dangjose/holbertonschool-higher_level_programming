#!/usr/bin/python3
"""Task 3. Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
        Args:
            obj: Object
            a_class: Class to search object

        Returns:
            Boolean
    """
    return isinstance(obj, a_class)
