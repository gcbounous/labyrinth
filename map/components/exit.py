# -*-coding:Utf-8 -*#
"""This module contains the class Exit."""
from obstacle import Obstacle

class Exit(Obstacle):

    """Defines an exit object (the exit of the labyrinth)."""

    def __init__(self, point = None):
        """
        """
        Obstacle.__init__(self, point, "*", True)
