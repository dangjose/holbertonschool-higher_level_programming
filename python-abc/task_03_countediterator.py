#!/usr/bin/python3
"""Task 3. CountedIterator - Keeping Track of Iteration"""


class CountedIterator():
    """
        Args:
            list
    """
    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
