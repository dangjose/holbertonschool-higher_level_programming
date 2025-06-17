#!/usr/bin/python3
"""Task 3. Area of a square"""


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
    def size(self, size):
        """Size setter"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
