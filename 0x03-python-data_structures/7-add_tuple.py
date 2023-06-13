#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    for i in range(2):
        list_a.append(0)
        list_b.append(0)

    sum_0 = list_a[0] + list_b[0]
    sum_1 = list_a[1] + list_b[1]
    tuple_c = (sum_0, sum_1)

    return tuple_c
