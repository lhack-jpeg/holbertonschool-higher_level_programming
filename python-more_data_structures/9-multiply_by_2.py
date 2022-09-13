#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    keys = a_dictionary.keys()
    for i in keys:
        value = a_dictionary.get(i) * 2
        new_dict.update({i: value})

    return new_dict
