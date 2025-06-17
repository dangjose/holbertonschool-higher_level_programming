#!/usr/bin/python3
"""Task 4. Access and update private attribute"""


class Square:
    """
        Defines a square

        Args:
            None

        Returns:
            Nothing
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2
