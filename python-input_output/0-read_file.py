#!/usr/bin/python3
"""Task 0. Read file"""

def read_file(filename=""):
    with open('UTF8.txt', 'r') as f:
        file = f.read()
        print(file)
