#!/usr/bin/python3
'''
This module contains one function
to append to file
'''


def append_write(filename="", text=""):
    '''
    Function to append to file
    '''
    with open(filename, "a", encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
