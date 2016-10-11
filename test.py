# -*-coding:Utf-8 -*#
import globals as globals_
from db.dbtext import DBText
from game import Game

db = DBText()
db.initialize()
print db.get_all_maps()

game  =  Game("lorilu", db.get_map('lorilu'))
print repr(game)

game.start()
print repr(game)

# TEST GAME functions
