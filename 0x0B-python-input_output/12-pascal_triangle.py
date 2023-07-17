#!/usr/bin/python3
"""
the 12-pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the pascal's
    triangle of n
    """
    plist = []
    if n <= 0:
        return plist
    tmp = []
    for i in range(n):
        a = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                a.append(1)
            else:
                a.append(tmp[j] + tmp[j - 1])
        tmp = a
        plist.append(tmp)
    return plist
