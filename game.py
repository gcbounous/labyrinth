# -*-coding:Utf-8 -*- #
"""This module contains the class Game."""
from map.components.point   import Point
from map.components.door    import Door
from map.components.exit    import Exit
from map.components.floor   import Floor
from map.components.robot   import Robot
from map.components.start   import Start
from map.components.wall    import Wall

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
        self._robot = Robot(robot_point)
        self._game_map = list()
        self._status = globals_.STATUS['NEW']

        self._populate_map(text)

    def start(self):
        """
            Method that starts a game, loading the robot if needed.
            It has the play loop as well.

            return 
                -the map if exit in the middle of the game or None, if game is finished
        """
        self._load_robot()
        self._play()

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
    def _populate_map(self, text):
        """
            Populates _game_map with map_objects by reading a "map text"
        """
        self._game_map = []
        x = 0
        y = 0
        for c in text:
            point = Point(x,y)

            if c == "\n":
                x = 0
                y += 1
            elif c == Door().get_symbol():
                self._game_map.append(Door(point))
                x += 1
            elif c == Exit().get_symbol():
                self._game_map.append(Exit(point))
                x += 1
            elif c == Start().get_symbol():
                self._game_map.append(Start(point))
                x += 1
            elif c == Wall().get_symbol():
                self._game_map.append(Wall(point))
                x += 1
            else:
                self._game_map.append(Floor(point))
                x += 1

    def _load_robot(self):
        """
            It sets the robot point the same as start. and sets start as a floor
            If it's a saved game (robot_point is not None and no start) it does nothing (already set in self._robot)
        """
  
        for i, obj in enumerate(self._game_map):
            if isinstance(obj, Start):
                point = obj.get_point()
                self._game_map[i] = Floor(point)

                self._robot.set_point(Point(point.get_x(),point.get_y()))
                break

    def _get_object_by_point(self, point):
        """
            Returns the object the is in that point if there is no object there returns None
        """
        for obj in self._game_map:
            if point == obj.get_point():
                return obj
        return None

    def _move_is_valid(self, move):
        """
            Verifies if the pressed key is an expected value and if there is room to move
            returns True or False if not a valid move
        """
        valid_move = False
        tmp_obj = None

        if move in globals_.KEYS.values():
            if move == globals_.KEYS['UP']:
                robot_point = self._robot.get_point()
                tmp_obj = self._get_object_by_point(Point(robot_point.get_x(), robot_point.get_y()-1))

            elif move == globals_.KEYS['DOWN']:
                robot_point = self._robot.get_point()
                tmp_obj = self._get_object_by_point(Point(robot_point.get_x(), robot_point.get_y()+1))

            elif move == globals_.KEYS['RIGHT']:
                robot_point = self._robot.get_point()
                tmp_obj = self._get_object_by_point(Point(robot_point.get_x()+1, robot_point.get_y()))

            elif move == globals_.KEYS['LEFT']:
                robot_point = self._robot.get_point()
                tmp_obj = self._get_object_by_point(Point(robot_point.get_x()-1, robot_point.get_y()))

            elif move == globals_.KEYS['QUIT']:
                valid_move = True

            if tmp_obj is not None and tmp_obj.is_passable():
                    valid_move = True

        return valid_move

    def _print_map(self):
        """
            Prints current game_map state 
        """
        os.system("clear")
        # os.system("setterm -cursor off")
        # os.system("setterm -cursor on")
        print str(self)

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

    def _is_end_of_game(self):
        """
            If the robot has arrived in the exit end_of_game is True
        """
        end_of_game = False
        robot_point = self._robot.get_point()
        obj = self._get_object_by_point(Point(robot_point.get_x(), robot_point.get_y()))
        if isinstance(obj, Exit):
            end_of_game = True
        return end_of_game

    def _play(self):
        """
            Game loop.
        """
        self._status = globals_.STATUS['IN_PLAY']

        while True:
            self._print_map() 
            move = self._on_key_press()
            while not self._move_is_valid(move):
                move = self._on_key_press()

            if move == globals_.KEYS['QUIT']:
                print 'quit'
                break

            self._robot.walk(move)
            
            if self._is_end_of_game():
                self._print_map()
                print "---- YOU WIN!! ----"

                self._status = globals_.STATUS['OVER']
                break

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
