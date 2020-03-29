# -*-coding:Utf-8 -*- #
"""This module contains the class Game."""
from map.components.point   import Point
from game_map               import GameMap
from utils.getch          import getch

import utils.globals as globals_

class Game:
    """Defines a game object. Is the acctual game populated with it's map component objects."""

    def __init__(self, name, text, robot_point = None):
        """
        """
        self._name = name
        self._game_map = GameMap(text, robot_point)
        self._status = globals_.Status.NEW
        self._visible_map = None

    def start(self):
        """
            Method that starts a game, loading the robot if needed.
            It leaves the game ready to be played.
        """
        self._game_map.load_robot()
        if self._visible_map is None:
            self._visible_map = GameMap(robot_point = self._game_map.get_robot_point())
            self._visible_map.append(self._game_map.get_new_room(self._visible_map))

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

    def print_map(self, visible_only = True):
        """
            Cleans terminal and prints map
        """
        os.system("clear")
        # os.system("cls") # windows
        if visible_only:
            self._visible_map.print_map()
        else:
            self._game_map.print_map()

    ####  private functions ###
    def _on_key_press(self):
        """
            Method that allows to the input on the key stroke without showing in the terminal
        """
        return getch()

    def _play(self):
        """
            Game loop.
        """
        self._status = globals_.Status.IN_PLAY
        known_door_points = list()

        while True:
            self.print_map()
            self._print_keys()

            move = self._on_key_press()
            # move = input() # windows
            while not self._game_map.move_is_valid(move):
                move = self._on_key_press()
                # move = input() # windows

            if move == globals_.KEYS['QUIT']:
                print('quit')
                break

            self._game_map.move_robot(move)

            if self._game_map.robot_at_door():
                current_point = self._game_map.get_robot_point()
                current_point = Point(current_point.get_x(),current_point.get_y())
                if current_point not in known_door_points:
                    self._visible_map.append(self._game_map.get_new_room(self._visible_map, move))
                    known_door_points.append(current_point)

            if self._game_map.is_end_of_game():
                self.print_map()
                self._status = globals_.Status.OVER
                print("---- YOU WIN!! ----")
                break

    def _print_keys(self):
        """
            Prints the keys to be used to play
        """
        keys = ""
        for name, k in globals_.KEYS.items():
            if name != 'QUIT':
                keys = "{}\n{}\t-\t[{}]".format(keys, name, k)
        keys = "{}\n{}\t-\t[{}]".format(keys, 'QUIT', globals_.KEYS['QUIT'])

        print(keys)

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
    print('oi')
    #test in test.py
