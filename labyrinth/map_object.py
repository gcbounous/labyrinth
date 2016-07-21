# -*-coding:Utf-8 -*
import Point
"""This module contains the class MapObject."""

class MapObject:

    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol):
        """
        """
        self.point = Point(point)
        self symbol = symbol

    def __repr__(self):
        """
        """
        return "<MapObject: ({}), symbol: {} >".format(self.point, self.symbol)

    def __str__(self):
        """
        """
        return self.symbol
