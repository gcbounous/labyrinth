# -*-coding:Utf-8 -*#

"""This module contains the class Robot."""

class Robot(MapObject):

    """Defines the robot contained in the map."""

    def __init__(self, point):
        """
        """
        MapObject.__init__(self, point, "@")

    def __repr__(self):
        """
        """
        return "<Robot ({1}): ({0})>".format(self.point, self.symbol)
