# -*-coding:Utf-8 -*
"""This module contains the class MapObject."""
from point import Point

class MapObject:
    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol):
        """
        """
        self.point = point
        self.symbol = symbol

    def get_symbol(self):
        """
        """
        return self.symbol

    def get_point(self):
        """
        """
        return self.point

    def __repr__(self):
        """
        """
        return str(self)

    def __str__(self):
        """
        """
        return self.symbol

if __name__ == "__main__":
    map_o = MapObject(Point(1,1), "\o")
    print repr(map_o)
    print str(map_o)
    print map_o
