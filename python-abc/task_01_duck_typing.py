#!/usr/bin/python3
"""Task 1. Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
        Args:
            ABC
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """
        Args:
            Shape
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
        Args:
            Shape
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

def shape_info(Shape):
    print("Area:", Shape.area())
    print("Perimeter:", Shape.perimeter())
