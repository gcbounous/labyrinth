# -*-coding:Utf-8 -*#
import os

# GLOBAL VARIABLES #

DB_DIR = "{}/db/".format(os.getcwd())
DB_TEXT_PATH = "{}dbtext.db".format(DB_DIR)
DB_SQL_PATH = "{}dbsql.db".format(DB_DIR)
MAPS_DIR = "{}/map/".format(os.getcwd())
MAPS_DEFAULT = "{}default/".format(MAPS_DIR)
MAPS_PERSONAL = "{}personal/".format(MAPS_DIR)

KEYS = {
		'UP': 'w',
		'RIGHT': 'd',
		'DOWN': 's',
		'LEFT': 'a',
		'QUIT': 'q'
		}

STATUS = {
		'IN_PLAY': 0,
		'OVER': 1,
		'NEW': 2	
		}

# DECORATORS #

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
				}
