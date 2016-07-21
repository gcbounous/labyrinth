# -*-coding:Utf-8 -*#

"""This module contains the class Door."""

class Door(Obstacle):

    """Defines a door object."""

    def __init__(self, point):
        """
        """
        Obstacle.__init__(self, point, "*", True)

    def __repr__(self):
        """
        """
        return "<Door ({1}): ({0})>".format(self.point, self.symbol)
