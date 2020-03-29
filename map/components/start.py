# -*-coding:Utf-8 -*#
"""This module contains the class Start."""
from map.components.map_object import MapObject

class Start(MapObject):
    """Defines an start object (where the robot will start in the map)."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, "_", True, point)
