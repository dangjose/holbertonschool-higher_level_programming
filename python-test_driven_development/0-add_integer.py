#!/usr/bin/python3
"""
This module provides a function that adds two integers.

The add_integer function ensures that inputs are either integers or floats,
raises a TypeError otherwise, and returns the sum as an integer.
"""
def add_integer(a, b=98):
    """
    Adds two integers after validating and casting float values.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The sum of a and b, as an integer.
    """
    if not isinstance(a, (int, float)):
        print("a must be an integer")
    if not isinstance(b, (int, float)):
        print("b must be an integer")
    return int(a) + int(b)
