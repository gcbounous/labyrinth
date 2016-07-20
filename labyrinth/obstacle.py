# -*-coding:Utf-8 -*#

"""This module contains the class Obstacle."""

class Obstacle(Map_Object):

    """Defines any object that can be contained in a map."""

    def __init__(self, point):
        self.point = point

    def __repr__(self):
        return "<Map_Object {}>".format(self.point)
