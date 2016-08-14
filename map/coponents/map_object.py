# -*-coding:Utf-8 -*
"""This module contains the class MapObject."""
from point import Point

class MapObject:
    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol):
        """
        """
        self._point = point
        self._symbol = symbol

    def get_symbol(self):
        """
        """
        return self._symbol

    def get_point(self):
        """
        """
        return self.poit

    def __repr__(self):
        """
        """
        return "<MapObject: {}, symbol: {} >".format(self._point, self._symbol)

    def __str__(self):
        """
        """
        return "<{1} : {0}  >".format(self._point, self._symbol)

if __name__ == "__main__":
    map_o = MapObject(Point(1,1), "\o")
    print repr(map_o)
    print str(map_o)
    print map_o
