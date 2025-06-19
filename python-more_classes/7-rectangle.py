#!/usr/bin/python3
"""Task 1. Real definition of a rectangle"""


class Rectangle:
    """
        Empty class

        Args:
            None

        Returns:
            Nothing
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area perimeter"""
        return (self.height * self.width)

    def perimeter(self):
        """Calculate perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * self.height + 2 * self.width

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        return '\n'.join(str(self.print_symbol) * self.width for item in range(self.height))

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
