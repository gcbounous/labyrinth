# -*-coding:Utf-8 -*

"""This module contains the class Point."""

class Point:

    """Defines a point in the map."""

# TODO: Has to receive a point, a tuple, a list, a dictionary or two values
    def __init__(self, x, y):
        """
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        """
        return "<Point ({},{})>".format(self.x, self.y)
