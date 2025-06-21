#!/usr/bin/python3
"""Task 1. My list"""

class MyList(list):
    """
        Args:
            list: class

        Returns:
            Nothing
    """
    def print_sorted(self):
        """Sorted List"""
        return sorted(self)
