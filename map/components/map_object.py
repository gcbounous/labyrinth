# -*-coding:Utf-8 -*
"""This module contains the class MapObject."""
from map.components.point import Point

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

    def __eq__(self, other):
        """
            Defines obj == other
            it is equal is they are at the same place (have same point)
        """
        return self._point == other._point

    def __ne__(self, other):
        """
            Defines obj != other
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
            Defines obj < other
        """
        return self._point < other._point

    def __gt__(self, other):
        """
            Defines point > other
        """
        return self._point > other._point

    def __le__(self, other):
        """
            Defines point <= other
        """
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        """
            Defines point >= other
        """
        return self.__eq__(other) or self.__gt__(other)

    def __hash__(self):
        """
        """
        return hash(self._point)

if __name__ == "__main__":
    map_1 = MapObject("lç", True, Point(1,1))
    map_2 = MapObject("\o", True, Point(1,1))

    print(map_1 == map_2)
