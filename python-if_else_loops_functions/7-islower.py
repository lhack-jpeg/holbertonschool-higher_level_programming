#!/usr/bin/python3
def islower(c):
    ascii_val = ord(c)
    print(ascii_val)
    if ascii_val >= 97 and ascii_val <= 123:
        return True
    else:
        return False
