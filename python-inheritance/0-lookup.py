#!/usr/bin/python3
"""Task 0. Lookup"""


def lookup(obj):
    """
        Args:
            obj: Object to list from

        Returns:
            The list of available attributes and methods of an object.
    """
    return dir(obj)
