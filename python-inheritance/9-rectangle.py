#!/usr/bin/python3
"""
module documentation
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    function documentation
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[{str(self.__class__.__name__)}] /
        {str(self.__width)}/{str(self.__height)}"

    def area(self):
        return self.__width * self.__height
