# -*-coding:Utf-8 -*#
import os

# GLOBAL VARIABLES #

""" paths """
DB_DIR = "{}/db/".format(os.getcwd())
DB_TEXT_PATH = "{}dbtext.db".format(DB_DIR)
DB_SQL_PATH = "{}dbsql.db".format(DB_DIR)
MAPS_DIR = "{}/map/".format(os.getcwd())
MAPS_DEFAULT = "{}default/".format(MAPS_DIR)
MAPS_PERSONAL = "{}personal/".format(MAPS_DIR)

""" keys dictionnary """
KEYS = {
		'UP': 'w',
		'RIGHT': 'd',
		'DOWN': 's',
		'LEFT': 'a',
		'QUIT': 'q'
		}

""" map status class (enum-like)"""
class Status:
    IN_PLAY, OVER, NEW = range(3)


# DECORATORS #

""" singleton decorator -> can only create 1 instance"""
def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


# DEFAULT MAPS #

DEFAULT_MAPS = {
				'prison':
						"OOOOOOOOOOOOOOOOOOOO\n"
						"O_O . O    O .     O\n"
						"O.O O O    O O     O\n"
						"O O O O    O O     O\n"
						"O.O O .    O O     O\n"
						"O O O OOOOOO O     O\n"
						"O O O        O     O\n"
						"O O OOOOOOOOOO     O\n"
						"O.O .        O     O\n"
						"O O O        O     O\n"
						"O O O        O     O\n"
						"O O.O        O     O\n"
						"O.O .        O     O\n"
						"O O O        O     O\n"
						"O O O        O     O\n"
						"O O O        O     O\n"
						"O O O        O     O\n"
						"O.O O        O     O\n"
						"O   O        O     *\n"
						"OOOOOOOOOOOOOOOOOOOO\n"
						,
				'easy':
						"OOOOOOOOOO\n"
						"O O    O O\n"
						"O . OO   O\n"
						"O O O    O\n"
						"O OOOO O.O\n"
						"O_O O    *\n"
						"O OOOOOO.O\n"
						"O O      O\n"
						"O O OOOOOO\n"
						"O . O    O\n"
						"OOOOOOOOOO\n"
						,
				'empty':
						"OOOOOOOOOOO\n"
						"O         O\n"
						"O         O\n"
						"O         O\n"
						"O         O\n"
						"O    _    O\n"
						"O         O\n"
						"O         O\n"
						"O         O\n"
						"O         *\n"
						"OOOOOOOOOOO\n"
						,
				"Maricota":
						"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n"
						"O_    O    .       O         .        . O\n"
						"OOOOO O OO.OO OOOO O.OOOO    O OOOOOO.O O\n"
						"O   O O O   O O  . O    OOOO.OOO    . O O\n"
						"O O O O OOO O O  OOOOOO O  O     OOOO O O\n"
						"O O . O   O O OO O .    O OOOOOOOO  O O O\n"
						"O OOO.OOO O O  O O OOOOOO.OOO .     . O O\n"
						"O  O    . O .  O O O  .       OOOOOOO . O\n"
						"O  O    OOO OOOO O O OO OOOOO .     OOOOO\n"
						"O OOOOO.O   OO O O O OO O . O OOOOO .   O\n"
						"O     O      O .   O .  O O O .     OOO O\n"
						"OOOOO OOOOOOOO OOOOO OOOO O O OOOOOOO O O\n"
						"O   O O    O       O O O  O O O  . .  O O\n"
						"O   O . OO OOOOOOO O O O  . O O  O O  O O\n"
						"O O O.OOOO O       O O O.OOOO OOOO.OOOO O\n"
						"O OOO O  . O O.OOOOO O      . .  O    . O\n"
						"O     O  O O O O     O.O.OOOO.OO O    O.O\n"
						"OOOOOOO  O O O O O   O O   O   O OOOOOO O\n"
						"O        O . O   OOOOO O OOOOO . O      O\n"
						"O   O.OOOO.O O.OOO  O  O  O O  O.OOOOOOOO\n"
						"O.OOO      O O      O OO  O O OO   O    O\n"
						"O   OOOOOOOO OOOOOO.O OOO O O.OOOO O O  *\n"
						"O          O        O .   O      O . OOOO\n"
						"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n"

				}
