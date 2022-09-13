#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sorted_keys = []
    for i in keys:
        sorted_keys.append(i)
    sorted_keys.sort()
    for i in sorted_keys:
        print("{}: {}".format(i, a_dictionary[i]))
