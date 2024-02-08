#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represent rectangle."""

    def __init__(self, width=0, height=0):
        self._Rectangle__heigh = height
        self._Rectangle__width = width


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        return self._Rectangle__height


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
