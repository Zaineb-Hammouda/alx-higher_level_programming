#!/usr/bin/python3
"""defines the MyList class"""


class MyList(list):
    """inherits from list class"""
    def print_sorted(self):
        """ prints sorted list"""
        print(sorted(self))
