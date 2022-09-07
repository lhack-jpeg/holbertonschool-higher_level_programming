#!/usr/bin/python3


def remove_char_at(str, n):
    if n >= 0:
        res_str = str[:n] + str[n+1:]
    else:
        res_str = str[:n-1] + str[n-1:]
    return res_str
