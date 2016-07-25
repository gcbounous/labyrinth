# -*-coding:Utf-8 -*#
"""This module contains the class Robot."""
from map_object import MapObject

class Robot(MapObject):
    """Defines the robot contained in the map."""

    def __init__(self, point):
        """
        """
        MapObject.__init__(self, point, "@")

    def __repr__(self):
        """
        """
        return "<Robot ({}): {}>".format(self.symbol, self.point)

    def walk(direction, sapaces = 1):
        """
        """


if __name__ == '__main__':
    print raw_input()
