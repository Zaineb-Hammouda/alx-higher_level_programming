#!/usr/bin/python3
"""
the 2-append_file module
"""


def append_write(filename="", text=""):
    """
    appends a string to a text file

    filename: the name of file
    text: the text string
    """
    with open(filename, 'a', encoding="utf-8") as f:
        appended = f.write(text)
    f.close()
    return appended
