# -*-coding:Utf-8 -*#
import globals as globals_
from db.dbtext import DBText

db = DBText()
db.initialize()

print db.get_map('prison')
db.new_user('Mari')
db.new_user("Gab")