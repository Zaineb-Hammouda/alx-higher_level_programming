#!/usr/bin/python3
"""
the 0-read_file module
"""


def read_file(filename=""):
    """
    reads from file and prints to stdout
    filename: the name of file to read and print
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
    f.close()

