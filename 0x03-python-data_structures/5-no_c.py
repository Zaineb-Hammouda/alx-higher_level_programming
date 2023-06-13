#!/usr/bin/python3
def no_c(my_string):
    new_s = ''
    for char in my_string:
        if char not in 'Cc':
            new_s += char
    return new_s
    """
    other option:
    my_string = my_string.translate({ord(i): None for i in 'Cc'})
    return my_string
    """
