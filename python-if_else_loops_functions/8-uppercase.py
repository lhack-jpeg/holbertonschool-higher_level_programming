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
        if index < len(str) - 1:
            if islower(elem):
                print("{:c}".format(ord(elem) - 32), end="")
            else:
                print("{:c}".format(ord(elem)), end="")
        else:
            if islower(elem):
                print("{:c}".format(ord(elem) - 32), end="\n")
            else:
                print("{:c}".format(ord(elem)), end="\n")
