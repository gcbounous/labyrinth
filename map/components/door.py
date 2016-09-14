# -*-coding:Utf-8 -*#
"""This module contains the class Door."""
from obstacle import Obstacle

class Door(Obstacle):

    """Defines a door object."""

    def __init__(self, point = None):
        """
        """
        Obstacle.__init__(self, point, ".", True)
