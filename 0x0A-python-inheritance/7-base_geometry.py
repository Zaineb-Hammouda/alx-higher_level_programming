#!/usr/bin/python3
""" the 7-base_geometry module"""


class BaseGeometry:
    """ BaseGeometry class"""
    def area(self):
        """ raises an execption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
