#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list is not None:
        is_div = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                is_div.append(True)
            else:
                is_div.append(False)
        return is_div
