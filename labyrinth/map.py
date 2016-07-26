# -*-coding:Utf-8 -*#
"""This module contains the class Map."""
from obstacle import Obstacle
from robot import Robot

class Map:
    """Defines a map object."""

    def __init__(self, name, text):
        """
        """
        self.name = name


    def __repr__(self):
        """
        """
        return "<Obstacle: {}, symbol: {}, passable: {} >".format(self.point, self.symbol, self.passable)
