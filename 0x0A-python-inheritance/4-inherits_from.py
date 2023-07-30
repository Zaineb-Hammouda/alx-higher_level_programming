#!/usr/bin/python3
""" the 4-inherits_from module"""


def inherits_from(obj, a_class):
    """ returns true if obj is instance of a class that inherits from
    specified class otherwise False"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
