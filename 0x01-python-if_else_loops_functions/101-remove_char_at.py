#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = "" + str
    if n > len(str) or n < 0:
        return(str1)
    else:
        return(str1.replace(str1[n], ''))

