#!/usr/bin/python3
'''
This module contains the one function read_file
'''


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
