#!/usr/bin/python3
"""Task 0. Read file"""


def read_file(filename=""):
    '''
        Reads a text file and print to stdout

        Args:
            filename: File to be read.

        Returns:
            Nothings
    '''
    with open(filename, 'r') as f:
        file = f.read()
        print(file, end='')
