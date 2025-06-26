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
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    except Exception:
        raise TypeError

def load_and_deserialize(filename):
    '''
        Load and deserialize data from a specified file.

        Args:
            filename: Name of file to be deserialized.

        Returns:
            Deserialized data
    '''
    try:
        with open (filename, 'rb') as f:
            return pickle.load(f)
    except (pickle.UnpicklingError, AttributeError) as e:
        raise e
