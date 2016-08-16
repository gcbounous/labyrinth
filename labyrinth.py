# -*-coding:Utf-8 -*#
"""This module contains the class Labyrinth."""
from game import Game
from db.dbtext import DBText
from db.dbsql import DBSql

class Labyrinth():

    """Defines a wall object."""

    def __init__(self, db = "text"):
        """
        """
        self._game = None


        self._game_main()

    def _game_main(self):
        """
        """
        #  TODO:
        #     - "login"
        #     - load menu: new game (get maps)/ saved games (get saved maps)/ map_editor
        #     - play
        self._login()

    def _login(self):
        """
        """
        user = raw_input("Type your user name: ")


