#!/usr/bin/python3
"""
the json model
"""
import json


def load_from_json_file(filename):
    """
    creates an obj from a JSON file
    """
    with open(filename, encoding="utf-8") as f:
        x = json.load(f)
