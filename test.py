# -*-coding:Utf-8 -*#
import utils.globals as globals_
from db.dbtext import DBText
from game import Game
from map.components.point   import Point
from map.components.door    import Door
from map.components.exit    import Exit

from labyrinth import Labyrinth

db = DBText()
db.initialize()

print(db.get_all_users())
# game  =  Game("lorilu", db.get_map("Maricota"))

# game.start()

# lab = Labyrinth()
