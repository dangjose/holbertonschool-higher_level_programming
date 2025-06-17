#!/usr/bin/python3
"""Task 2. Size validation"""


class Square:
    """
        Defines a square

        Args:
            None

        Returns:
            Nothing
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def __size(self, size):
        """Size setter"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
