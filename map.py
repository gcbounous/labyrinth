# -*-coding:Utf-8 -*#
"""This module contains the class Map."""
import map.components as components
from components.obstacle import Obstacle
from components.robot import Robot

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
