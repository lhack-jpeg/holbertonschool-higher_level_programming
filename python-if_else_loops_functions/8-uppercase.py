#!/usr/bin/python3


def islower(c):
    ascii_val = ord(c)

    if ascii_val >= 97 and ascii_val <= 123:
        return True
    else:
        return False


def uppercase(str):
    for elem in str:
        if islower(elem):
            elem = chr(ord(elem) - 32)

        print("{}".format(elem), end="")
    print("")
