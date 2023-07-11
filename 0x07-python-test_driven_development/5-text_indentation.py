#!/usr/bin/python3
"""
5-text_indentation module
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these chars:
    '.', '?' and ':'
    text: the text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for i in range(len(text)):
        if flag == 0:
            if text[i] == " ":
                continue
            else:
                flag = 1
        if flag:
            if text[i] in ['.', '?', ':']:
                print(text[i])
                print()
                flag = 0
            else:
                print(text[i], end="")
