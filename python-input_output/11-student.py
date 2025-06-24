#!/usr/bin/python3
"""Task 11. Student to disk and reload"""


class Student:
    """
        Defines a student

        Args:
            None

        Returns:
            Nothing
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            result = {}
            for item in attrs:
                if isinstance(item, str):
                    if hasattr(self, item):
                        result[item] = getattr(self, item)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            setattr(self, key, json[key])
