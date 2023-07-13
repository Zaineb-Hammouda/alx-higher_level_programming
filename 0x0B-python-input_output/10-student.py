#!/usr/bin/python3
"""
defines a class student
"""


class Student:
    """ defines a class student"""
    def __init__(self, first_name, last_name, age):
        """ initializes public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dic rep of a student instance """
        a_dict = {}
        if attrs is not None:
            for a in attrs:
                try:
                    a_dict[a] = self.__dict__[a]
                except Exception:
                    pass
            return a_dict
        else:
            return self.__dict__
