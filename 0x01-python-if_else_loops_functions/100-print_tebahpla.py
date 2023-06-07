#!/usr/bin/python3
for char in range(122, 96, -1):
    if char % 2 == 0:
        char = chr(char)
    else:
        char = chr(char - 32)
    print("{}".format(char), end="")
