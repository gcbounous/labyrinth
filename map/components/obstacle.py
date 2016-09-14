# -*-coding:Utf-8 -*#
"""This module contains the class Obstacle."""
from map_object import MapObject

class Obstacle(MapObject):
    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol, passable):
        """
        """
        MapObject.__init__(self, point, symbol)
        self.passable = passable

    def is_passable(self):
        """
            Returns true if the obstacle is passable
        """
        return self.passable
