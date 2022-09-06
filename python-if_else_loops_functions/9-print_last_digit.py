#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        value = ((number * -1) % 10)
    else:
        value = number % 10

    print("{}".format(value), end="")
    return value
