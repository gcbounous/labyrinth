# -*-coding:Utf-8 -*#
"""This module contains the class Exit."""
from map_object import MapObject

class Exit(MapObject):

    """Defines an exit object (the exit of the labyrinth)."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, "*", True, point)
