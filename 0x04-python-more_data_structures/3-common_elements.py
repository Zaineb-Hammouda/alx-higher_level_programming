#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for i in set_1:
        for j in set_2:
            if j == i:
                my_list.append(j)
                my_set = set(my_list)
    return my_set
