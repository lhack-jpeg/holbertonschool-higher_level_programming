#!/usr/bin/python3


if __name__ == '__main__':
    import hidden_4
    import sys

    for name in dir(hidden_4):
        if name[0] != '_':
            print("{:s}".format(name))
