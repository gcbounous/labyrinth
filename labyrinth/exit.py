# -*-coding:Utf-8 -*#

"""This module contains the class Exit."""

class Exit(Obstacle):

    """Defines an exit object."""

    def __init__(self, point):
        """
        """
        Obstacle.__init__(self, point, " ", True)

    def __repr__(self):
        """
        """
        return "<Exit ({1}): ({0})>".format(self.point, self.symbol)
