# -*-coding:Utf-8 -*#
"""This module contains the class Labyrinth."""
from game import Game
from db.dbtext import DBText
from db.dbsql import DBSql

import globals as globals_

import os

class Labyrinth():

    """Defines the main class wich the game takes place."""

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
        self._main_menu()

    def _login(self):
        """
        """
        os.system("clear")
        # os.system("cls") # windows
        
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
            'N': self._new_game,
            'L': self._load_game,
            'P': self._preferences,
        }
        menu_ok = False
        while not menu_ok:
            self._print_main_menu()
            menu = raw_input()
            try:
                if menu.isdigit():
                    menu = int(menu)
                else:
                    menu = menu.upper()
                assert ((menu > 0 and menu <= len(dic_menu)/2+1) or (menu in 'NLPQ' and len(menu) == 1))
            except:
                # ERROR
                print("Please choose a valid menu number or letter.")
                raw_input()
            else:
                if menu == 4 or menu == 'Q':
                    menu_ok = True
                else:
                    function = dic_menu[menu]
                    menu_ok = function()
        self._quit()

    def _new_game(self):
        """
        """
        quit = False
        menu_ok = False
        while not menu_ok:
            os.system("clear")
            # os.system("cls") # windows

            map_names = []
            maps = self._db.get_all_maps()
            menu_string = "{}, in what map do you want to play?\n\n".format(self._user_name)
            for i,map_name in enumerate(maps.keys()):
                map_names.append(map_name)
                menu_string += "{}) {}\n".format(i, map_name)
            menu_string += "\n{}) {}{}R{}eturn to main menu.\n".format(len(map_names),'\033[1m','\033[4m','\033[0m')
            menu_string += "{}) {}{}Q{}uit".format(len(map_names)+1,'\033[1m','\033[4m','\033[0m')
            print(menu_string)

            menu = raw_input()
            try:
                if menu.isdigit():
                    menu = int(menu)
                else:
                    menu = menu.upper()
                assert ((menu >= 0 and menu <= len(map_names)+1) or (menu in 'RQ' and len(menu) == 1))
            except:
                # ERROR
                print("Please choose a valid map number or letter.")
                raw_input()
            else:
                if menu == len(map_names) or menu == 'R':
                    quit = False
                    menu_ok = True
                elif menu == len(map_names)+1 or menu == 'Q':
                    quit = True
                    menu_ok = True
                else:
                    map_name = map_names[menu]
                    print(maps[map_name])
                    game = Game(map_name, maps[map_name])
                    game.print_map(visible_only = False)

                    menu_ok = self._load_map_and_play(game)

        return quit

    def _load_game(self):
        """
        """
        self._user = self._db.get_user(self._user_name)
        if len(self._user) == 0:
            print("{}, you have no saved games. (press Enter to return to the main menu)".format(self._user_name))
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
                    print("{}) {}".format(i, game_name))

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

            return False

    def _load_map_and_play(self, game):
        """
            return True if wants to return to main menu
        """
        print("\nLoad this map? (Y/N)")
        menu = raw_input().upper()
        while menu not in "YN" or len(menu) != 1:
            print("Load this map? (Y/N)")
            menu = raw_input().upper()

        if menu != "Y":
            return False
        else:
            game.start()
            game_status = game.get_status()
            if game_status == globals_.Status.IN_PLAY:
                self._save_game(game)

            print("Load another game? (Y/N)".format(self._user_name))
            menu = raw_input().upper()
            while menu not in "YN" or len(menu) != 1:
                print("Load another game? (Y/N)".format(self._user_name))
                menu = raw_input().upper()

            if menu == 'Y':
                return False
            else:
                return True

    def _save_game(self, game):
        """
        """
        print("{}, do you want to save you game progression? (Y/N)".format(self._user_name))
        menu = raw_input().upper()
        while menu not in "YN" or len(menu) != 1:
            print("{}, do you want to save you game progression? (Y/N)".format(self._user_name))
            menu = raw_input().upper()

        if menu == "Y":
            self._db.save_user_game(self._user_name, game.get_name(), game)

    def _preferences(self):
        """
        """
        print("pref")
        pass

    def _quit(self):
        """
        """
        print("BYE BYE, {}!!".format(self._user_name))

    def _print_main_menu(self):
        """
        """
        os.system("clear")
        # os.system("cls") # windows
        menu = "\n- {}, choose a menu option:".format(self._user_name)
        menu += "\n(1) {0}{1}N{2}ew game \n(2) {0}{1}L{2}oad game \n(3) {0}{1}P{2}references \n(4) {0}{1}Q{2}uit".format('\033[1m','\033[4m','\033[0m')
        print(menu)


if __name__ == '__main__':
    labyrinth = Labyrinth()

