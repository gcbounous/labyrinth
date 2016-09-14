# -*-coding:Utf-8 -*#
"""This module contains the class Robot."""
from map_object import MapObject

class Robot(MapObject):
    """Defines the robot contained in the map."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, point, "@")

    def walk(direction, sapaces = 1):
        """
        """
        pass

if __name__ == '__main__':
    print raw_input()
