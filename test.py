# -*-coding:Utf-8 -*#
import globals as globals_
from db.dbtext import DBText
from game import Game

db = DBText()
db.initialize()

game  =  Game("lorilu", db.get_map('easy'))
print repr(game)

game.start()
print repr(game)

# TEST GAME functions
