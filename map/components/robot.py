# -*-coding:Utf-8 -*#
"""This module contains the class Robot."""
from map_object import MapObject
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
        print 'up'
        pass

    def move_down(self):
        """
        """
        print 'down'
        pass

    def move_right(self):
        """
        """
        print 'right'
        pass

    def move_left(self):
        """
        """
        print 'left'
        pass

if __name__ == '__main__':
    print raw_input()
