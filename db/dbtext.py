# -*-coding:Utf-8 -*#
"""This module contains the class DBText."""
import utils.globals as globals_
import os
import pickle

@globals_.singleton
class DBText():
    """
        Defines a text data base. It saves all the maps users and saved games
        Data structure:
            maps : {map_name : map_te }                       *without robot
            users : { user_name: {map_name : game_object } }  *with robot
    """
    def __init__(self):
        """
            Constructor that initializes the data-base object
        """
        self.maps = {}
        self.users = {}

    def initialize(self):
        """
            Method that populates the object attributes
        """
        #TODO: to be removed and db must be fixed
        self._load_personal_maps()
        self._load_default_maps()

        # if os.path.isfile(globals_.DB_TEXT_PATH):
        #     self._load_db()
        # else:
        #     self._load_personal_maps()
        #     self._load_default_maps()
        #     self._write_db()

    def get_all_maps(self):
        """
            Method that returns all maps
        """
        self._load_db()
        return self.maps

    def get_all_users(self):
        """
            Method that returns all users
        """
        self._load_db()
        return self.users

    def get_map(self, map_name):
        """
            Method that returns a map if it exists
            params:
                - map_name
        """
        self._load_db()
        try:
            return self.maps[map_name]
        except KeyError:
            print("Map '{}' doesn't exist.".format(map_name))
            return None

    def get_user(self, user_name):
        """
            Method that returns a user if it exists
            param:
                - user_name
        """
        self._load_db()
        try:
            return self.users[user_name]
        except KeyError:
            print("User-id '{}' doesn't exist.".format(user_name))
            return None

    def get_saved_game(self, user_name, game_name):
        """
            Mathod that returns a saved game
            params:
                - user_name
                - game_name
        """
        game = None
        self._load_db()
        if user_name in self.users.keys():
            user = self.users[user_name]
            if game_name in user.keys():
                game = user[game_name]
            else:
                print("Game '{}' doesn't exist.".format(game_name))
        else:
            print("User-id '{}' doesn't exist.".format(user_name))
        return game

    def new_user(self, user_name):
        """
            Method that saves a new user
            param:
                - user_name
        """
        self._load_db()
        if user_name not in self.users.keys():
            self.users[user_name] = {}
            self._write_db()
            return True
        else:
            print("User-id '{}' already exists.".format(user_name))
            return False

    def new_map(self, map_name, map_text):
        """
            Method that saves a new map
            params:
                - map_name
                - map_text
        """
        self._load_db()
        if map_name not in self.maps.keys():

            if not os.path.isdir(globals_.MAPS_PERSONAL):
                os.mkdir(globals_.MAPS_PERSONAL)

            map_file = "{}.txt".format(map_name)
            with open("{}{}".format(globals_.MAPS_PERSONAL,map_file), 'w') as file_:
                file_.write(map_text)
            self.maps[map_name] = map_text
            self._write_db()
            return True
        else:
            print("Map with name '{}' already exists.".format(map_name))
            return False

    def save_user_game(self, user_name, game_name, game):
        """
            Method that saves a user game in play
            params:
                - user_name
                - game_name
                - game
        """
        self._load_db()
        if user_name in self.users.keys():
            self.users[user_name][game_name] = game
            self._write_db()
        else:
            print("User-id '{}' doesn't exist.".format(user_name))

    ####  private functions ###
    def _load_default_maps(self):
        """
            Method that gets the default maps described in globals
        """
        for map_name,map_text in globals_.DEFAULT_MAPS.items():
            self.maps[map_name] = map_text

    def _load_personal_maps(self):
        """
            Method that gets the maps in the personnal_maps folder
        """
        if not os.path.isdir(globals_.MAPS_PERSONAL):
                os.mkdir(globals_.MAPS_PERSONAL)

        for f_name in os.listdir(globals_.MAPS_PERSONAL):
            with open("{}{}".format(globals_.MAPS_PERSONAL,f_name), 'r') as file_:
                self.maps[f_name.split(".")[0]] = file_.read()

    def _write_db(self):
        """
            Method that refreshes the data base
        """
        with open(globals_.DB_TEXT_PATH, 'wb') as file_:
            my_pickler = pickle.Pickler(file_)
            my_pickler.dump(self)

    def _load_db(self):
        """
            Method that loads the data base information into the dsata base object
        """
        # with open(globals_.DB_TEXT_PATH, 'rb') as file_:
        #     my_unpickler = pickle.Unpickler(file_)
        #     loaded_db = my_unpickler.load()
        #     self.maps = loaded_db.maps
        #     self.users = loaded_db.users
        pass

if __name__ == '__main__':
    print("test with labyrinth/test.py to reduce import problems")