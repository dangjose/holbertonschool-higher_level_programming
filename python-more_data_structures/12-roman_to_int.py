#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    last_value = 0

    for char in reversed(roman_string):
        value = r_dict[char]
        if value < last_value:
            total -= value
        else:
            total += value
        last_value = r_dict[char]

    return total
