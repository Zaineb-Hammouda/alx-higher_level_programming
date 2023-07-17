#!/usr/bin/python3
"""
the 100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts text to file after each line containing specific string
    @filename: the file name
    @search_string: the string to insert after
    @new_string: the string to insert
    """
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readlines()
        for line in read:
            if search_string in line:
                read.insert(read.index(line) + 1, new_string)
        text = ''.join(read)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
