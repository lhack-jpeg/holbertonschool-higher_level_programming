#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    print_total = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_total += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()

    return print_total
