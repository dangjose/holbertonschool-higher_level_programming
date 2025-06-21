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
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
