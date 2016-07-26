# -*-coding:Utf-8 -*#
"""This module contains the class DBSql."""
import os

class DBSql():
    """Defines a SQL data base."""

    DB_PATH = "./dbsql.db"
    DEFAUL_MAPS = "./default_maps/"

    def __init__(self):
        """
        """
        self.maps = {}
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
            self.write_db

    def _load_default_maps(self):
        """
        """
        pass

    def write_db(self):
        """
        """
        pass

    def load_db(self):
        """
        """
        pass

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
