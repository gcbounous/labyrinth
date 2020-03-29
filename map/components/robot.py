# -*-coding:Utf-8 -*#
"""This module contains the class Robot."""
from map_object import MapObject
from point import Point
import globals as globals_

class Robot(MapObject):
    """Defines the robot contained in the map."""

    def __init__(self, point = None):
        """
        """
        MapObject.__init__(self, "@", False, point)

    def walk(self, direction, sapaces = 1):
        """
        """
        if direction in globals_.KEYS.values():
            if direction == globals_.KEYS['UP']:
                self.move_up()
            elif direction == globals_.KEYS['DOWN']:
                self.move_down()
            elif direction == globals_.KEYS['RIGHT']:
                self.move_right()
            elif direction == globals_.KEYS['LEFT']:
                self.move_left()

    def move_up(self):
        """
        """
        self._point.set_y(self.get_point().get_y()-1)

    def move_down(self):
        """
        """
        self._point.set_y(self.get_point().get_y()+1)

    def move_right(self):
        """
        """
        self._point.set_x(self.get_point().get_x()+1)

    def move_left(self):
        """
        """
        self._point.set_x(self.get_point().get_x()-1)

if __name__ == '__main__':
    print(raw_input())
