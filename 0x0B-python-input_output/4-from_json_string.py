#!/usr/bin/python3
"""
the json module
"""
import json


def from_json_string(my_str):
    """
    returns object represented by json str
    my_str: the json string
    """
    return json.loads(my_str)
