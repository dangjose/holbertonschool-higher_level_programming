#!/usr/bin/python3
"""Task 1. Pickling Custom Classes"""

import pickle


class CustomObject:
    '''Objects to be serialized and deserialized'''

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''Print object attributes'''

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''
            Serialize and save instance to a specified file.

            Args:
                filename: Name of file to save serialized instance to.
        '''
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''
            Load and deserialize instance from a specified file.

            Args:
                filename: Name of file to be deserialized.

            Returns:
                Deserialized instance
        '''
        try:
            with open(filename, 'wb') as f:
                return pickle.load(f)
        except Exception:
            return None
