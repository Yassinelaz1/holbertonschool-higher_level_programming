#!/usr/bin/python3
"""
Module documentation
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string repsentation  of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value
        
    def __update(self, id=None, size=None, x=None, y=None):
        """ updates """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
    