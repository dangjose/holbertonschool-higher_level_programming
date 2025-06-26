#!/usr/bin/python3
"""Task 0. Basic Serialization"""

import pickle


def serialize_and_save_to_file(data, filename):
    '''
        Serialize and save data to a specified file.

        Args:
            data: Material to serialize and save.
            filename: Name of file to save data to.
    '''
    with open(filename, 'wb') as f:
        pickle.dump(data, filename)

def load_and_deserialize(filename):
    '''
        Load and deserialize data from a specified file.

        Args:
            filename: Name of file to be deserialized.

        Returns:
            Deserialized data
    '''
    with open (filename, 'rb') as f:
        return pickle.load(f)
