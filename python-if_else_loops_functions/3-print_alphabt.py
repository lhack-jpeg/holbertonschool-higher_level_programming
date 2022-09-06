#!/usr/bin/python3
for j in range(ord('a'), ord('z') + 1):
    if (j == ord('e') or j == ord('q')):
        continue
    else:
        print("{:c}".format(j), end="")
