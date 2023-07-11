#!/usr/bin/python3
"""
3-say_my_name module
contains the say_my_name() function
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name() prints my name is <firs name> <last name>
    first_name: the first name
    last_name: the last name
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
