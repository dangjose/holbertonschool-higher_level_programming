#!/usr/bin/python3
"""Task 5. The Mystical Dragon - Mastering Mixins"""


class SwimMixin:
    """
        Mixin
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
        Mixin
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
        Args:
            SwimMixin, FlyMixin
    """
    def roar(self):
        print("The dragon roars!")
