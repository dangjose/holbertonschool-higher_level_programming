#!/usr/bin/python3
"""Task 0. Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
        Args:
            ABC
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
        Args:
            Animal
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
        Args:
            Animal
    """
    def sound(self):
        return "Meow"
