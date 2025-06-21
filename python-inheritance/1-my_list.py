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
        print(sorted(self))
