#!/usr/bin/python3
""" 100-my_int module"""


class MyInt(int):
    """ inherits from int"""
    def __eq__(self, other):
        """the equality method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ the inequality method"""
        return super().__eq__(other)
