#!/usr/bin/python3
"""Task 1. Write to a file"""


def write_file(filename="", text=""):
    '''
        Writes a string to text file.

        Args:
            filename: File to write to.
            text = Statement to write.

        Returns:
            Number of characters written
    '''
    with open(filename, 'w') as f:
        return f.write(text)
