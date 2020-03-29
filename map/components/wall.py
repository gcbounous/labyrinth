# -*-coding:Utf-8 -*#
"""This module contains the class Wall."""
from map.components.map_object import MapObject

class Wall(MapObject):

    """Defines a wall object."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, "O", False, point)

