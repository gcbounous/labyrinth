# -*-coding:Utf-8 -*#

"""This module contains the class Obstacle."""

class Obstacle(MapObject):
    """Defines any object that can be contained in a map."""

    def __init__(self, point, symbol, passable):
        """
        """
        MapObject.__init__(self, point, symbol)
        self.passable = passable

    def __repr__(self):
        """
        """
        return "<Obstacle: ({}), symbol: {}, passable: {} >".format(self.point, self.symbol, self.passable)
