#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Define a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """initialize method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """position method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) is not int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):

        return (self.__size*self.__size)

    def my_print(self):
        """Print the square using the character #."""
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
