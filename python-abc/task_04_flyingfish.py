#!/usr/bin/python3
"""Task 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance"""


class Fish:
    """
        Fish Properties
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
        Bird Properties
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
        Args:
            Fish, Bird
    """
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
