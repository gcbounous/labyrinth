# -*-coding:Utf-8 -*
"""This module contains the class MapObject."""
import point

class MapObject:
    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol):
        """
        """
        self.point = Point(point)
        self.symbol = symbol

    def __repr__(self):
        """
        """
        return "<MapObject: ({}), symbol: {} >".format(self.point, self.symbol)

    def __str__(self):
        """
        """
        return "<{1}: ({0})  >".format(self.point, self.symbol)

    def get_symbol(self):
        """
        """
        return self.symbol

    def get_point(self):
        """
        """
        return self.poit
