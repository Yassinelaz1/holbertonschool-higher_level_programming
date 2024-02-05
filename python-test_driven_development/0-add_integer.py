#!/usr/bin/python3
"""
    This function takes two parameters, 'a' and 'b'

    Parameters:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
    int: The sum of 'a' and 'b', converted to an integer.

    Raises:
    TypeError: If 'a' or 'b' is not an integer or a float.
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
