#!/usr/bin/python3
'''
Module contains a function to go through text and format
a specific way.
'''


def text_indentation(text):
    '''
    Function goes through text and searches for [?, :, .].
    If characters are found two new lines are printed out.
    If text is not string raies TypeError.
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    text = text.strip()

    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char in ["?", ":", "."]:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
