#!/usr/bin/python3
"""Task 10. Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Args:
            Rectangle class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area"""
        return self.__size ** 2
