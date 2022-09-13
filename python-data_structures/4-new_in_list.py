#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list is not None:
        if idx >= len(my_list) or idx < 0:
            return None
        copy_list = my_list.copy()
        copy_list[idx] = element

        return copy_list
