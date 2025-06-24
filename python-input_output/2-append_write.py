#!/usr/bin/python3
"""Task 2. Append to a file"""


def append_write(filename="", text=""):
    '''
        Appends a string at the end of a text file.

        Args:
            filename: File to append to.
            text = Statement to append.

        Returns:
            Number of characters added
    '''
    with open(filename, 'a') as f:
        return f.write(text)
