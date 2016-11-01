# -*-coding:Utf-8 -*#
"""This module contains the class Labyrinth."""
from game import Game
from db.dbtext import DBText
from db.dbsql import DBSql

import globals as globals_

import os

class Labyrinth():

    """Defines a wall object."""

    def __init__(self, db = "text"):
        """
            self._user: dict with all the users saved game
        """
        self._user = None
        self._user_name = ""
        self._db = DBText()

        self._game_main()

    def _game_main(self):
        """
        """
        self._db.initialize()
        self._login()

        quit = False
        while not quit:
            quit = self._main_menu()

    def _login(self):
        """
        """
        self._user_name = raw_input("Type your user name: ").upper()
        all_users_dict = self._db.get_all_users()

        if self._user_name in all_users_dict.keys():
            self._user = all_users_dict[self._user_name]
        else:
            self._db.new_user(self._user_name)

    def _main_menu(self):
        """
        """
        dic_menu = {
            1: self._new_game,
            2: self._load_game,
            3: self._preferences,
            4: self._quit
        }
        menu_ok = False
        while not menu_ok:
            self._print_main_menu()
            menu = raw_input()
            try:
                menu = int(menu)
                assert (menu > 0 and menu <= len(dic_menu))
            except:
                # ERROR
                print("Please choose a valid menu number.")
            else:
                menu_ok = True

        function = dic_menu[menu]
        quit = function()
        return quit

    def _new_game(self):
        """
        """
        print "new"
        # return quit

    def _load_game(self):
        """
        """
        if len(self._user) == 0:
            print "{}, you have no saved games. (press Enter to return to the main menu)"
            raw_input()
            return False
        else:
            menu_ok = False
            while not menu_ok:
                os.system("clear")
                # os.system("cls") # windows

                game_names = []
                for i,game_name in enumerate(self._user.keys()):
                    game_names.append(game_name)
                    print "{}) {}".format(i, game_name)

                menu = raw_input()
                try:
                    menu = int(menu)
                    assert (menu >= 0 and menu < len(self._user))
                except:
                    # ERROR
                    print("Please choose a valid game number.")
                else:
                    game = self._user[game_names[menu]]
                    game.print_map()

                    menu_ok = self._load_map_and_play(game)

            function = dic_menu[menu]
            quit = function()
            return quit

    def _load_map_and_play(self, game):
        """
        """
        print "Load this map? (Y/N)"
        menu = raw_input().upper()
        while menu not in "YN" or len(menu) != 1:
            print "Load this map? (Y/N)"
            menu = raw_input().upper()

        if menu == "N":
            return False
        else:
            game.start()
            game_status = game.get_status()
            if game_status == globals_.Status.IN_GAME:
                self._save_game(game)

    def _save_game(self, game):
        """
        """
        print "Do you want to save you game progression? (Y/N)"
        menu = raw_input().upper()
        while menu not in "YN" or len(menu) != 1:
            print "Do you want to save you game progression? (Y/N)"
            menu = raw_input().upper()

        if menu == "Y":
            self._db.save_user_game(self._user_name, game.get_name(), game)

    def _preferences(self):
        """
        """
        print "pref"
        pass

    def _quit(self):
        """
            Returns true to quit
        """
        return True

    def _print_main_menu(self):
        """
        """
        os.system("clear")
        # os.system("cls") # windows
        menu = "\n- Choose a menu option:"
        menu += "\n(1) New game \n(2) Load game \n(3) Preferences \n(4) Quit"
        print(menu)

