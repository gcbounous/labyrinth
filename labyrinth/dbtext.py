# -*-coding:Utf-8 -*#
"""This module contains the class DBText."""
import os
import pickle

class DBText():

    """Defines a text data base."""

    DB_PATH = "./dbtext"

    def __init__(self):
        """
        """
        self.maps = []
        self.users = []
        self.load_games = {}

        self.initialize_db()

    def initialize_db(self):
        """
        """
        if os.path.isfile(self.DB_PATH):
            self.load_db()

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
        pass

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
    db.maps.append(0)
    db.maps.append(1)
    db.maps.append(2)
    db.write_db()
    print(db.maps)
    db.maps = "ferrou"
    print(db.maps)
    db.load_db()
    print(db.maps)
