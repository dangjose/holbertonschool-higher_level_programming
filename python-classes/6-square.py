#!/usr/bin/python3
"""Task 6. Coordinates of a square"""


class Square:
    """
        Defines a square

        Args:
            None

        Returns:
            Nothing
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @size.setter
    def position(self, value):
        """Position setter"""
        if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
        for num in value:
            if num < 0 or not isinstance(num, int):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print('_' * self.__position[0] + '#' * self.__size)
