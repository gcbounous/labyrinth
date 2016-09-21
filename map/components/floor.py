# -*-coding:Utf-8 -*#
"""This module contains the class Floor."""
from map_object import MapObject

class Floor(MapObject):
    """Defines the Floor contained in the map."""

    def __init__(self, point = None):
        """
        """        
        MapObject.__init__(self, " ", True, point)


if __name__ == '__main__':
    print raw_input()
