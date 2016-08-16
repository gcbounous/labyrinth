# -*-coding:Utf-8 -*#
"""This module contains the class Game."""
from map.components.obstacle import Obstacle
from map.omponents.robot import Robot

class Game:
    """Defines a game object. Is the acctual game populated with it's map component objects."""

    def __init__(self, name, text):
        """
        """
        self.name = name


    def __repr__(self):
        """
        """
        return "<Obstacle: {}, symbol: {}, passable: {} >".format(self.point, self.symbol, self.passable)
