#!/usr/bin/python3
""" 101-add_attribute module"""


def add_attribute(obj, name, value):
    """ adds a new attrb to an obj if possible"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
