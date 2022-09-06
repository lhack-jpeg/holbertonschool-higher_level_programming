#!/usr/bin/python3
i = 0
while i < 9:
    j = i + 1
    while j < 10:
        if i < 8:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j), end="\n")
        j = j + 1
    i = i + 1
