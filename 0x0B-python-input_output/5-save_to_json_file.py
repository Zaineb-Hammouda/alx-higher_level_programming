#!/usr/bin/python3
"""
the json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes a json rep of an obj to a text file
    """
    rep = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(rep)
    f.close()
