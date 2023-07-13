#!/usr/bin/python3
"""
the 1-write_file module
"""


def write_file(filename="", text=""):
    """
    writes a strings to a text file

    filename: the name of file
    text: the text string
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write = f.write(text)
    f.close()
    return write
