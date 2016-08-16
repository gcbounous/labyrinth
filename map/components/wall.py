# -*-coding:Utf-8 -*#
"""This module contains the class Wall."""
from obstacle import Obstacle

class Wall(Obstacle):

    """Defines a wall object."""

    def __init__(self, point):
        """
        """
        Obstacle.__init__(self, point, "O", False)

    def __repr__(self):
        """
        """
        return "<Wall ({}): {}>".format(self.symbol, self.point)
