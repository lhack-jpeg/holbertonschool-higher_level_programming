#!/usr/bin/python3

def islower(c):
    ascii_val = ord(c)

    if ascii_val >= 97 and ascii_val <= 123:
        return True
    else:
        return False


def uppercase(str):
    for index in range(0, len(str)):
        elem = str[index]
        if islower(elem):
            elem = chr(ord(str[index]) - 32)

        if index < len(str) - 1:
            print("{:c}".format(ord(elem)), end="")
        else:
            print("{:c}".format(ord(elem)), end="\n")
