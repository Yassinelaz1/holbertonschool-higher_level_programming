#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represent rectangle."""

def __init__(self, width=0, height=0):
    """Initialize a new Rectangle.

    Args:
        width (int): The width 
        height (int): The height
    """
    self.width = width
    self.heigh = height


@property
def width(self):
    return self.__width


@width
def width(self, value):
    if not isinstance(value, int):
        raise TypeError(width must be an integer)
    if value < 0:
        raise ValueError("width must be >= 0")
    return self.__width


@property
def height(self):
    return self.__height


@height
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    return self.__height
