#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mod_num = ((number * -1) % 10) * -1
else:
    mod_num = number % 10


if mod_num > 5:
    print(f"Last digit of {number:d} is {mod_num:d} and is greater than 5")
elif mod_num < 6 and mod_num != 0:
    print(f"Last digit of {number:d} is {mod_num:d} \
and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {mod_num:d} and is 0")
