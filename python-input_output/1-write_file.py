#!/usr/bin/python3
'''
This Module contains one function to write to a file
'''


def write_file(filename="", text=""):
    '''
    This function writes to file and returns amount
    of characters wrttien to file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        char_written = f.write(text)
        return (char_written)
