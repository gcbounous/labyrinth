# -*-coding:Utf-8 -*- #
"""This module contains the class GameMap."""
from map.components.point   import Point
from map.components.door    import Door
from map.components.exit    import Exit
from map.components.floor   import Floor
from map.components.robot   import Robot
from map.components.start   import Start
from map.components.wall    import Wall
from map.components.empty   import Empty

import globals as globals_

class GameMap:
    """Defines a game map object. Is the acctual map populated with it's map component objects."""

    def __init__(self, map_input = None, robot_point = None):
        """
            GameMap constructor, it can be constructed based on a text or a list of map_objects (we suppose the map is well constructed)
        """
        self._robot = Robot(robot_point)
        self._game_map = list()

        if isinstance(map_input, basestring):
            self._populate(map_input)
        elif isinstance(map_input, list):
            self._game_map = map_input
            self._game_map.sort()
        elif map_input is None:
            pass
        else:
            # ERROR!!
            self = None

    def get_game_map(self):
        """
        """
        return self._game_map

    def get_robot_point(self):
        """
        """
        return self._robot.get_point()

    def load_robot(self):
        """
            It sets the robot point the same as start. and sets start as a floor
            If it's a saved game (has no start) or a empty map it does nothing.
        """
        for i, obj in enumerate(self._game_map):
            if isinstance(obj, Start):
                point = obj.get_point()
                self._game_map[i] = Floor(point)
                self._robot.set_point(Point(point.get_x(),point.get_y()))
                break

    def append(self, obj_list):
        """
        """
        self._game_map += obj_list
        self._game_map.sort()
        self.clean_map()
        self._fill_map()

    def get_new_room(self, visible_map, last_move = None):
        """
            Method that loads the visible new room being limited by walls and doors.
            param
                - visible_map: list of the visible map objects

        """
        visible_map.clean_map()
        visible_map = visible_map.get_game_map()

        room_list = []
        has_neighbors = []
        current_point = Point(self._robot.get_point().get_x(), self._robot.get_point().get_y())

        if last_move == globals_.KEYS['UP']:
            current_point.set_y(current_point.get_y()-1)
        elif last_move == globals_.KEYS['DOWN']:
            current_point.set_y(current_point.get_y()+1)
        elif last_move == globals_.KEYS['RIGHT']:
            current_point.set_x(current_point.get_x()+1)
        elif last_move == globals_.KEYS['LEFT']:
            current_point.set_x(current_point.get_x()-1)

        has_neighbors.append(self._get_object_by_point(Point(current_point.get_x(), current_point.get_y())))
        while True:
            current_object = self._get_object_by_point(Point(current_point.get_x(), current_point.get_y()))
            room_list.append(current_object)

            obj_up = self._get_object_by_point(Point(current_point.get_x(), current_point.get_y()-1))
            obj_left = self._get_object_by_point(Point(current_point.get_x()-1, current_point.get_y()))
            obj_down = self._get_object_by_point(Point(current_point.get_x(), current_point.get_y()+1))
            obj_right = self._get_object_by_point(Point(current_point.get_x()+1, current_point.get_y()))

            if isinstance(current_object, Door) or isinstance(current_object, Exit):
                room_list.append(current_object)

                if isinstance(obj_up, Wall):
                    room_list.append(obj_up)
                if isinstance(obj_left, Wall):
                    room_list.append(obj_left)
                if isinstance(obj_down, Wall):
                    room_list.append(obj_down)
                if isinstance(obj_right, Wall):
                    room_list.append(obj_right)
            else:
                unwanted_objects = has_neighbors + visible_map + room_list

                if obj_up not in unwanted_objects: # look up                 
                    if isinstance(obj_up, Wall):
                        room_list.append(obj_up)

                        obj_point = obj_up.get_point()
                        obj_up_right = self._get_object_by_point(Point(obj_point.get_x()+1, obj_point.get_y()))
                        obj_up_left = self._get_object_by_point(Point(obj_point.get_x()-1, obj_point.get_y()))

                        if isinstance(obj_up_right, Wall):
                            room_list.append(obj_up_right)
                        if isinstance(obj_up_left, Wall):
                            room_list.append(obj_up_left)
                    else:
                        has_neighbors.append(obj_up)

                if obj_left not in unwanted_objects: # look left
                    if isinstance(obj_left, Wall):
                        room_list.append(obj_left)

                        obj_point = obj_left.get_point()
                        obj_left_up = self._get_object_by_point(Point(obj_point.get_x(), obj_point.get_y()-1))
                        obj_left_down = self._get_object_by_point(Point(obj_point.get_x(), obj_point.get_y()+1))

                        if isinstance(obj_left_up, Wall):
                            room_list.append(obj_left_up)
                        if isinstance(obj_left_down, Wall):
                            room_list.append(obj_left_down)
                    else:
                        has_neighbors.append(obj_left)

                if obj_down not in unwanted_objects: # look down
                    if isinstance(obj_down, Wall):
                        room_list.append(obj_down)

                        obj_point = obj_down.get_point()
                        obj_down_right = self._get_object_by_point(Point(obj_point.get_x()+1, obj_point.get_y()))
                        obj_down_left = self._get_object_by_point(Point(obj_point.get_x()-1, obj_point.get_y()))

                        if isinstance(obj_down_right, Wall):
                            room_list.append(obj_down_right)
                        if isinstance(obj_down_left, Wall):
                            room_list.append(obj_down_left)
                    else:
                        has_neighbors.append(obj_down)

                if obj_right not in unwanted_objects: # look right
                    if isinstance(obj_right, Wall):
                        room_list.append(obj_right)

                        obj_point = obj_right.get_point()
                        obj_right_up = self._get_object_by_point(Point(obj_point.get_x(), obj_point.get_y()-1))
                        obj_right_down = self._get_object_by_point(Point(obj_point.get_x(), obj_point.get_y()+1))

                        if isinstance(obj_right_up, Wall):
                            room_list.append(obj_right_up)
                        if isinstance(obj_right_down, Wall):
                            room_list.append(obj_right_down)
                    else:
                        has_neighbors.append(obj_right)

            has_neighbors.pop(0)
            if len(has_neighbors) > 0:
                current_point = has_neighbors[0].get_point()
            else:
                break

        room_list = list(set(room_list))
        return room_list

    def move_is_valid(self, move):
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

    def print_map(self):
        """
            Prints current game_map state
        """
        print str(self)

    def move_robot(self, move):
        """
        """
        self._robot.walk(move)

    def is_end_of_game(self):
        """
            If the robot has arrived in the exit end_of_game is True
        """
        end_of_game = False
        robot_point = self._robot.get_point()
        obj = self._get_object_by_point(Point(robot_point.get_x(), robot_point.get_y()))
        if isinstance(obj, Exit):
            end_of_game = True
        return end_of_game

    def robot_at_door(self):
        """
            Returns True if robot is currently over a Door
        """
        current_point = self._robot.get_point()
        current_object = self._get_object_by_point(current_point)
        if isinstance(current_object, Door):
            return True
        else:
            return False

    def clean_map(self):
        """
            Cleans doubles and empty objects
        """

        for obj in sorted(self._game_map, reverse = True):
            if isinstance(obj, Empty):
                self._game_map.remove(obj)
        self._game_map = list(set(self._game_map))
        self._game_map.sort()

    #### private functions ###
    def _fill_map(self):
        """
            fills map with empty object where there is nothing
        """
        x_bound, y_bound = self._get_bounds()

        for x in xrange(x_bound+1):
            for y in xrange(y_bound+1):
                empty = Empty(Point(x,y))
                if empty not in self._game_map:
                    self._game_map.append(empty)
        self._game_map.sort()

    def _populate(self, text):
        """
            Populates _game_map with map_objects by reading a "map text"
            @param text: text describing map with mep object symbols

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
        self._game_map.sort()

    def _get_object_by_point(self, point):
        """
            Returns the object the is in that point if there is no object there returns None
        """
        for obj in self._game_map:
            if point == obj.get_point():
                return obj
        return None

    def _get_bounds(self):
        """
            Returns the x and y bounds of the map
                obs: self._game_map is expected to be sorted
        """
        x_max = 0
        y_max = 0

        for obj in self._game_map:
            point = obj.get_point()
            if point.get_x() > x_max:
                x_max =  point.get_x()
            if point.get_y() > y_max:
                y_max =  point.get_y()

        return (x_max, y_max)

    def __repr__(self):
        """
        """
        return "<Game map: \n{}>".format(str(self))

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
