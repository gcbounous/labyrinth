# -*-coding:Utf-8 -*#
"""This module contains the class DBText."""
import os
import pickle

class DBText():
    """
    Defines a text data base. It saves all the maps users and saved games
    Data structure:
        maps : [map_objects]                        *without robot
        users : [names]                             *case sensetive
        saved_games : { user_name: [map_objects] }  *with robot
    """

    def __init__(self):
        """
        """
        self.maps = []
        self.users = []
        self.load_games = {}

        self._initialize_db()

    def _initialize_db(self):
        """
        """
        if os.path.isfile(self.DB_PATH):
            self.load_db()
        else:
            self._load_default_maps()
            self._load_personal_map()
            self.write_db()

    def _load_default_maps(self):
        """
        """
        for f_name in os.listdir(self.DEFAULT_MAPS):
            with open("{}{}".format(self.DEFAULT_MAPS,f_name), 'r') as file_:
                self.maps[f_name]= file_.read()

    def _load_personal_map(self):
        """
        """
        for f_name in os.listdir(self.PERSONAL_MAPS):
            with open("{}{}".format(self.PERSONAL_MAPS,f_name), 'r') as file_:
                self.maps[f_name]= file_.read()

    def write_db(self):
        """
        """
        with open(self.DB_PATH, 'wb') as file_:
            my_pickler = pickle.Pickler(file_)
            my_pickler.dump(self)

    def load_db(self):
        """
        """
        with open(self.DB_PATH, 'rb') as file_:
            my_unpickler = pickle.Unpickler(file_)
            loaded_db = my_unpickler.load()
            self.maps = loaded_db.maps
            self.users = loaded_db.users
            self.load_games = loaded_db.load_games

    def get_maps(self):
        """
        """
        self.load_db()
        return self.maps

    def get_map(self, map): #get by name?(id?)
        """
        """
        pass

    def new_map(self):
        """
        """
        pass

    def get_users(self):
        """
        """
        pass

    def set_new_user(self):
        """
        """
        pass

    def get_user_games(self, user): #get by name?(id?)
        """
        """
        pass

    def save_user_game(self, user, game): #by name?(id?)
        """
        """
        pass

    def load_user_game(self): #by name?(id?)
        """
        """
        pass

if __name__ == '__main__':
    db = DBText()
    for n,m in db.maps.items():
        print n
        print m
