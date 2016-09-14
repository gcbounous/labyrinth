# -*-coding:Utf-8 -*#
"""This module contains the class Start."""
from obstacle import Obstacle

class Start(Obstacle):
    """Defines an start object (where the robot will start in the map)."""

    def __init__(self, point = None):
        """
        """
        Obstacle.__init__(self, point, "_", True)
