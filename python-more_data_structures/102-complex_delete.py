#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary is not None:
        names = []
        for name, dict_value in a_dictionary.items():
            if dict_value == value:
                names.append(name)
        for name in names:
            a_dictionary.pop(name)
        return a_dictionary
    else:
        return None
