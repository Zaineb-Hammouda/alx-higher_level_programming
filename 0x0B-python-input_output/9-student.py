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

    def to_json(self):
        """ retrieves a dic rep of a student instance """
        return self.__dict__
