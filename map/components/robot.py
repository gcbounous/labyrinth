# -*-coding:Utf-8 -*#
"""This module contains the class Robot."""
from map_object import MapObject

class Robot(MapObject):
    """Defines the robot contained in the map."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, "@", False, point)

    def walk(self, direction, sapaces = 1):
        """
        """
        if move in globals_.KEYS:
            if move == globals_.KEYS['UP']:
                self.move_up()
            elif move == globals_.KEYS['DOWN']:
                self.move_down()
            elif move == globals_.KEYS['RIGHT']:
                self.move_right()
            elif move == globals_.KEYS['LEFT']:
                self.move_left()

    def move_up(self):
        """
        """
        pass

    def move_down(self):
        """
        """
        pass

    def move_right(self):
        """
        """
        pass

    def move_left(self):
        """
        """
        pass

if __name__ == '__main__':
    print raw_input()
