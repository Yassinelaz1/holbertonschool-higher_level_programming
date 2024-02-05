#!/usr/bin/python3
"""
    This function takes two parameters, 'a' and 'b'
"""


def add_integer(a, b=98):
    """
    Parameters:
    a : The first number to be added.
    b: The second number to be added.

    Returns:
    int: The sum of 'a' and 'b', converted to an integer.

    Raises:
    TypeError: If 'a' or 'b' is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
