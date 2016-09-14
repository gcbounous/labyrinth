# -*-coding:Utf-8 -*- #
"""This module contains the class Game."""
from map.components.point import Point
from map.components.door import Door
from map.components.exit import Exit
from map.components.floor import Floor
from map.components.robot import Robot
from map.components.start import Start
from map.components.wall import Wall

class Game:
    """Defines a game object. Is the acctual game populated with it's map component objects."""

    def __init__(self, name, text):
        """
        """
        self._name = name
        self._game_map = list()
        self._populate_map(text)

    def __repr__(self):
        """
        """
        return "<Game: name {}, \ntext: \n{}>".format(self._name, str(self))

    def __str__(self):
        """
            Tranforms the _game_map into text
        """
        game_text = ""
        row = 0
        for obj in self._game_map:
            if obj.get_point().get_y() == row + 1:
                game_text = "{}\n".format(game_text)
                row += 1        
            game_text = "{}{}".format(game_text, obj.get_symbol())
        return game_text

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
            elif c == Robot().get_symbol():
                self._game_map.append(Robot(point))
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
            If robot is not present it is loaded in the place of "start"
        """
        for i, obj in enumerate(self._game_map):
            if isinstance(obj, Start):
                point = obj.get_point()
                self._game_map[i] = Robot(point)

    def _play(self):
        """
            Game loop.
        """
        pass

    def start(self):
        """
            Method that starts a game, loading the robot if needed.
            It has the play loop as well.
            @return the map if exit in the middle of the game or None, if game is finished
        """
        robot_present = False
        for obj in self._game_map:
            if isinstance(obj, Robot):
                robot_present = True
                break
        if not robot_present:
            self._load_robot()

        self._play()

    def get_name(self):
        """
        """
        return self._name

    def get_game_map(self):
        """
        """
        return self._game_map

if __name__ == '__main__':
    pass
    # TODO: Test all functions in test.py
