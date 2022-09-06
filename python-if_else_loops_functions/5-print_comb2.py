#!/usr/bin/python3
for j in range(100):
    if j < 99:
        print("{:d}{:d}".format(j // 10, j % 10), end=", ")
    else:
        print("{:d}{:d}".format(j // 10, j % 10), end="\n")
