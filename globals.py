# -*-coding:Utf-8 -*#
import os

# GLOBAL VARIABLES #

DB_DIR = "{}/db/".format(os.getcwd())
DB_TEXT_PATH = "{}dbtext.db".format(DB_DIR)
DB_SQL_PATH = "{}dbsql.db".format(DB_DIR)
MAPS_DIR = "{}/map/".format(os.getcwd())
MAPS_DEFAULT = "{}default/".format(MAPS_DIR)
MAPS_PERSONAL = "{}personal/".format(MAPS_DIR)


# DECORATORS #

def singleton(cls):
    instances = {}
    
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance
