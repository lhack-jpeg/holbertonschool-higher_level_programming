#!/usr/bin/python3
"""Function to add two integers or floats."""


def add_integer(a, b=98):
    """
    Sums the value of the parameters passed through. Checks to see if value are
    of type int or float. Cast values to int before additon and returning.
    """
    if type(a) != int:
        if type(a) != float:
            raise TypeError("a must be an integer")
    if type(b) != int:
        if type(b) != float:
            raise TypeError("b must be an integer")

    return int(a) + int(b)
