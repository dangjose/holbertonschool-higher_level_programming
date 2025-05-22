#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_elem = len(argv) - 1

    def print_arg(elements):
        for i in range(1, len(elements)):
            print('{}: {}'.format(i, elements[i]))

    if num_elem == 0:
        print('0 arguments.')
    elif num_elem == 1:
        print('1 argument:')
        print_arg(argv)
    else:
        print('{} arguments:'.format(num_elem))
        print_arg(argv)
