#!/usr/bin/python3


def common_elements(set_1, set_2):
    common_items = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common_items.append(i)

    return common_items
