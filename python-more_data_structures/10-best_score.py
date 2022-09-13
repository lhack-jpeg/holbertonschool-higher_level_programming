#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        hi_score = 0
        for key in a_dictionary:
            if a_dictionary[key] > hi_score:
                hi_score = a_dictionary[key]
        for name, score in a_dictionary.items():
            if score == hi_score:
                return name
    else:
        return None
