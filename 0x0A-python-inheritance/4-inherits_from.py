#!/usr/bin/python3
""" the 4-inherits_from module"""


def inherits_from(obj, a_class):
    """ returns true if obj is instance of a class that inherits from
    specified class otherwise False"""
    if isinstance(obj, a_class) and a_class is not bool:
        return True
    else:
        return False
