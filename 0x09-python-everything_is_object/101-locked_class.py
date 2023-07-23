#!/usr/bin/python3
# 101-locked_class.py
"""101-locked_class module"""


class LockedClass:
    """ locked class that prevents the user from dynamically creating
    new instance attributes, except if the new instance attribute is
    called first_name"""
    __slots__ = ["first_name"]
