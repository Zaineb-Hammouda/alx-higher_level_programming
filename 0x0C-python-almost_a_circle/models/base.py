#!/usr/bin/python3
"""
the base module
defines a class Base
"""
import json
import os
import os.path


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the Json string rep json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attrs set"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                rectangle = cls(6, 5)
            else:
                rectangle = cls(6)
            rectangle.update(**dictionary)
            return rectangle

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename) is True:
            with open(filename, "r", encoding="utf-8") as f:
                read = f.read()
                jlist = Base.from_json_string(read)
                ilist = []
                for i in jlist:
                    instance = cls.create(**i)
                    ilist.append(instance)
                return ilist
        else:
            return []
