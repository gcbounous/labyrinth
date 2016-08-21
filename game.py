# -*-coding:Utf-8 -*#
"""This module contains the class Game."""
from map.components.obstacle import Obstacle
from map.omponents.robot import Robot

class Game:
    """Defines a game object. Is the acctual game populated with it's map component objects."""

    def __init__(self, name, text):
        """
        """
        self.name = name
        self.game_map = []
        self.game_map = populate_map(text)


    def __repr__(self):
        """
        """
        return "<Game: name {}, text: {}>".format(self.name, str(self))

    def __str__(self):
    	"""
    		Tranforms the game_map into text
    	"""
    	game_text = ""
    	for object in game_map:
    		
    	return game_text
