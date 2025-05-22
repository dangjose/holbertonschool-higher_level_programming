#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        abs_num = number * -1
        last_dig = abs_num % 10
        print(last_dig, end='')
        return (last_dig)
    else:
        last_dig = number % 10
        print(last_dig, end='')
        return (last_dig)
