# -*-coding:Utf-8 -*#
import globals as globals_
from db.dbtext import DBText
from game import Game
from map.components.point   import Point
from map.components.door    import Door
from map.components.exit    import Exit

db = DBText()
db.initialize()

game  =  Game("lorilu", db.get_map("Maricota"))

game.start()


# print sorted([obj.get_point() for obj in set([Door(Point(1,1)), Exit(Point(1,9)), Exit(Point(1,1)), Door(Point(1,2))])])
