#!/usr/bin/python3
"""Task 7. Integer validator"""


class BaseGeometry():
    """
        Args:
            None
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer"""
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
