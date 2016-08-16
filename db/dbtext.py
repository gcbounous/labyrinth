# -*-coding:Utf-8 -*#
"""This module contains the class DBText."""
import globals as globals_
import os
import pickle

@globals_.singleton
class DBText():
    """
    Defines a text data base. It saves all the maps users and saved games
    Data structure:
        maps : {map_name : [map_objects] }                  *without robot
        users : { user_name: {map_name : [map_objects] } }  *with robot
    """

    teste = globals_.DB_SQL_PATH

    def __init__(self):
        """
            Constructor that initializes the data-base object
        """
        self.maps = {}
        self.users = {}

    def _load_default_maps(self):
        """
            Method that gets the maps in the default_maps folder
        """
        for f_name in os.listdir(globals_.MAPS_DEFAULT):
            with open("{}{}".format(globals_.MAPS_DEFAULT,f_name), 'r') as file_:
                self.maps[f_name] = file_.read()

    def _load_personal_maps(self):
        """
            Method that gets the maps in the personnal_maps folder
        """
        for f_name in os.listdir(globals_.MAPS_PERSONAL):
            with open("{}{}".format(globals_.MAPS_PERSONAL,f_name), 'r') as file_:
                self.maps[f_name] = file_.read()

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
        with open(globals_.DB_TEXT_PATH, 'rb') as file_:
            my_unpickler = pickle.Unpickler(file_)
            loaded_db = my_unpickler.load()
            self.maps = loaded_db.maps
            self.users = loaded_db.users
 
    def initialize_db(self):
        """
            Method that populates the object attributes
        """
        if os.path.isfile(globals_.DB_TEXT_PATH):
            self._load_db()
        else:
            self._load_default_maps()
            self._load_personal_maps()
            self._write_db()

    def get_maps(self):
        """
            Method that returns all maps
        """
        self._load_db()
        return self.maps

    def get_users(self):
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
        except IndexError:
            print "Map '{}' doesn't exist.".format(map_name)
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
        except IndexError:
            print "User-id '{}' doesn't exist.".format(user_name)
            return None

    def get_user_game(self, user_name, game_name):
        """
            Mathod that returns a saved game
            params:
                - user_name
                - game_name
        """
        game_text = None
        self._load_db()
        if user_name in self.users.keys():
            user = self.users[user_name]
            if game_name in user.keys():
                game_text = user[game_name]
            else:
                print "Game '{}' doesn't exist.".format(game_name)
        else:
            print "User-id '{}' doesn't exist.".format(user_name)
        return game_text

    def set_new_user(self, user_name):
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
            print "User-id '{}' already exists.".format(user_name)
            return False

    def set_new_map(self, map_name, map_text):
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
            with open("{}{}".format(globals_.MAPS_PERSONAL,map_name), w) as file_:
                file.write(map_text)
            self.maps[map_name] = map_text
            self._write_db()
            return True
        else:
            print "Map with name '{}' already exists.".format(map_name)
            return False

    def save_user_game(self, user_name, game_name, game_text):
        """
            Method that saves a user game in play
            params:
                - user_name
                - game_name
                - game_text
        """
        if user_name in self.users.keys():
            self.users[user_name][game_name] = game_text
        else:
            print "User-id '{}' doesn't exist.".format(user_name)

if __name__ == '__main__':
    db = DBText()

    print globals_.DB_TEXT_PATH
