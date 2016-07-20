# -*-coding:Utf-8 -*

"""This module contains the class Map_Object."""

class Map_Object:

    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol):
        self.point = point
        self symbol = symbol

    def __repr__(self):
        return "<Map_Object {}>".format(self.point)
