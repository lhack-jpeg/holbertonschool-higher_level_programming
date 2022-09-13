#!/usr/bin/python3


def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0

    total = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    strlen = len(roman_string)
    for i in range(strlen - 1, -1, -1):
        value = roman_dict[roman_string[i]]
        if i <= strlen - 2:
            if value < roman_dict.get(roman_string[i + 1]):
                value *= -1
        total += value

    return total
