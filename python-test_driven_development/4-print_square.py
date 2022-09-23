#!/usr/bin/python3
"""Module that prints out a square using # character."""


def print_square(size):
    """
    Function that prints out a square with size being the width.
    The function checks to ensure that size is of good value. Raises
    errors otherwise
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
