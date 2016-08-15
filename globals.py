# -*-coding:Utf-8 -*#

DB_TEXT_PATH = "./db/dbtext.db"
DB_SQL_PATH = "./db/dbsql.db"
MAPS_DIR = "./maps/"
MAPS_DEFAULT = "{}{}".format(MAPS_DIR,"default/")
MAPS_PERSONAL = "{}{}".format(MAPS_DIR,"personal/")

def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance
