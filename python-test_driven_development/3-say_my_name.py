#!/usr/bin/python3
"""Module to print out the persons name"""


def say_my_name(first_name, last_name=""):
    """
    Takes the first name and last name and concatenates the two onto
    a template string. Checks to ensure the values passed through are
    strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
