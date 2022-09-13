#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    new_val = {key: value}
    a_dictionary.update(new_val)
    return a_dictionary
