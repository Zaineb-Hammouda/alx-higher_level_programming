#!/usr/bin/python3
"""
the base module
defines a class Base
"""
import json


class Base:
    """
    defines a class instance base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes public instance attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep of list_dictionnaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = []
                for i in list_objs:
                    dicts.append(i.to_dictionary())
                f.write(Base.to_json_string(dicts))
