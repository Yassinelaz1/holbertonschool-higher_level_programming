#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square. Defaults to 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the new square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
