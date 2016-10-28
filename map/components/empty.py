# -*-coding:Utf-8 -*#
"""This module contains the class Floor."""
from map_object import MapObject

class Empty(MapObject):
    """Defines the Empty space or not known parts of the map contained in the map."""

    def __init__(self, point = None):
        """
        """        
        MapObject.__init__(self, "e", False, point)


if __name__ == '__main__':
    print raw_input()
