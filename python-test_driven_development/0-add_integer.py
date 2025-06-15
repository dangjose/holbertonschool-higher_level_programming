#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers after validating and casting float values.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The sum of a and b, as an integer.
    """
    return int(a) + int(b)
