#!/usr/bin/python3

import sys

argc = len(sys.argv) - 1

if (argc == 1):
    print("{:d} argument:".format(argc))
elif argc == 0:
    print("{:d} arguments.".format(argc))
else:
    print("{:d} arguments:".format(argc))

for i in range(1, argc + 1):
    print("{:d}: {:s}".format(i, sys.argv[i]))
