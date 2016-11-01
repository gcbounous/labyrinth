# -*-coding:Utf-8 -*#
import globals as globals_
from db.dbtext import DBText
from game import Game
from map.components.point   import Point
from map.components.door    import Door
from map.components.exit    import Exit

from labyrinth import Labyrinth

db = DBText()
db.initialize()

game  =  Game("lorilu", db.get_map("Maricota"))

game.start()

# lab = Labyrinth()
