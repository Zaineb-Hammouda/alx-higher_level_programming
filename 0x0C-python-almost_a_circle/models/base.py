#!/usr/bin/python3
"""
the base module
defines a class Base
"""


class Base:
    """
    defines a class instance base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        initializes public instance attributes
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
