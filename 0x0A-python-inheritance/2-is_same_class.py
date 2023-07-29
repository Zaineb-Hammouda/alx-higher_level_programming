#!/usr/bin/python3
""" the 2-is_same_class module"""


def is_same_class(obj, a_class):
    """ returns true if obj is instance of specified class
    otherwise False"""
    return type(obj) is a_class
