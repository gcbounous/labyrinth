# -*-coding:Utf-8 -*
"""This module contains the class MapObject."""
from point import Point

class MapObject:
    """Defines any object that can be contained in a map."""

    def __init__(self, symbol, passable, point = None):
        """
        """
        self._point = point
        self._symbol = symbol
        self._passable = passable

    def get_symbol(self):
        """
        """
        return self._symbol

    def get_point(self):
        """
        """
        return self._point

    def set_point(self, point):
        """
        """
        self._point = point

    def is_passable(self):
        """
            Returns true if the obstacle is passable
        """
        return self._passable

    def __repr__(self):
        """
        """
        return str(self)

    def __str__(self):
        """
        """
        return self._symbol

if __name__ == "__main__":
    map_o = MapObject(Point(1,1), "\o")
    print repr(map_o)
    print str(map_o)
    print map_o
