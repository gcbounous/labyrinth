# -*-coding:Utf-8 -*#
"""This module contains the class Door."""
from map.components.map_object import MapObject

class Door(MapObject):

    """Defines a door object."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, ".", True, point)
