#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = "" + str
    if n > len(str1) or n < 0:
        print(str1)
    else:
        print(str1.replace(str1[n], ''))
