#!/usr/bin/python3
""" the lookup fucntion """


def lookup(obj):
    """
    returns a list of methods and attrs of an obj"""
    return list(dir(obj))
