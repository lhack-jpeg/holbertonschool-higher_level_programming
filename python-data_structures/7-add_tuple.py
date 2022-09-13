#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_c = []
    while len(list_a) < 2:
        list_a.append(0)
    while len(list_b) < 2:
        list_b.append(0)

    for i in range(2):
        list_c.append(list_a[i] + list_b[i])

    tuple_c = tuple(list_c)
    return (tuple_c)
