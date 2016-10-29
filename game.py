# -*-coding:Utf-8 -*- #
"""This module contains the class Game."""
from map.components.point   import Point
from game_map               import GameMap

import globals as globals_

import os
import sys
import termios
import tty

class Game:
    """Defines a game object. Is the acctual game populated with it's map component objects."""

    def __init__(self, name, text, robot_point = None):
        """
        """
        self._name = name
        self._game_map = GameMap(text, robot_point)
        self._status = globals_.Status.NEW

    def start(self):
        """
            Method that starts a game, loading the robot if needed.
            It has the play loop as well.

            return
                -the map if exit in the middle of the game or None, if game is finished
        """
        self._game_map.load_robot()
        os.system("setterm -cursor off")
        self._play()
        os.system("setterm -cursor on")

    def get_name(self):
        """
        """
        return self._name

    def get_status(self):
        """
        """
        return self._status

    def get_game_map(self):
        """
        """
        return self._game_map

    ####  private functions ###
    def _on_key_press(self):
        """
            Method that allows to the input on the key stroke without sowing in the terminal
            Reference:
                - http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/
        """
        stdin_file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(stdin_file_descriptor)
        try:
            tty.setraw(stdin_file_descriptor)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(stdin_file_descriptor, termios.TCSADRAIN, old_settings)
        return ch

    def _play(self):
        """
            Game loop.
        """
        self._status = globals_.Status.IN_PLAY

        visible_map = GameMap(robot_point = self._game_map.get_robot_point())
        visible_map.append(self._game_map.get_new_room(visible_map))
        known_door_points = list()

        while True:
            self._print_map(visible_map)

            move = self._on_key_press()
            # move = raw_input() # windows
            while not self._game_map.move_is_valid(move):
                move = self._on_key_press()
                # move = raw_input() # windows

            if move == globals_.KEYS['QUIT']:
                print 'quit'
                break

            self._game_map.move_robot(move)

            if self._game_map.robot_at_door():
                current_point = self._game_map.get_robot_point()
                current_point = Point(current_point.get_x(),current_point.get_y())
                if current_point not in known_door_points:
                    visible_map.append(self._game_map.get_new_room(visible_map, move))
                    known_door_points.append(current_point)

            if self._game_map.is_end_of_game():
                self._print_map(visible_map)
                self._status = globals_.Status.OVER
                print "---- YOU WIN!! ----"
                break

    def _print_map(self, visible_map):
        """
            Cleans terminal and prints map
        """
        os.system("clear")
        # os.system("cls") # windows
        visible_map.print_map()

    def __repr__(self):
        """
        """
        return "<Game: name {},\ntext: \n{}>".format(self._name, str(self))

    def __str__(self):
        """
            Tranforms the _game_map into text
        """
        game_text = ""
        robot_point = self._robot.get_point()
        row = 0
        for obj in self._game_map:
            if robot_point is not None and obj.get_point() == robot_point:
                obj = self._robot
            if obj.get_point().get_y() == row + 1:
                game_text = "{}\n".format(game_text)
                row += 1
            game_text = "{}{}".format(game_text, obj.get_symbol())
        return game_text

if __name__ == '__main__':
    print 'oi'
    #test in test.py
