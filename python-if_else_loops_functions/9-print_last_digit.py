#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        abs_num = number * -1
        return (abs_num % 10)
    else:
        return (number % 10)
