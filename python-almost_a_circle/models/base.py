#!/usr/bin/python3
"""
module documentation
"""
import json
from os.path import isfile

class Base:
    """
    function documentation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as f:
                json.dump([], f)
        else:
            objs = list(i.to_dictionary() for i in list_objs)
            with open(f"{cls.__name__}.json", "w") as f:
                f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            x = list(json.loads(json_string))
            return x

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            uptd = Rectangle(1, 1)
        elif cls is Square:
            uptd = Square(1)
        else:
            uptd = None
        uptd.update(**dictionary)
        return uptd

    @classmethod
    def load_from_file(cls):
        file="{}.json".format(cls.__name__)
        if isfile(file):
            with open(file,"r") as f:
                j_str = f.read()
                l = cls.from_json_string(j_str)
                return [cls.create(**i) for i in l]
        else:
            return[]

