# -*-coding:Utf-8 -*#
"""This module contains the class Start."""
from obstacle import Obstacle

class Start(Obstacle):
    """Defines an start object (where the robot will start in the map)."""

    def __init__(self, point):
        """
        """
        Obstacle.__init__(self, point, "_", True)

    def __repr__(self):
        """
        """
        return "<Start ({}): {}>".format(self.symbol, self.point)
