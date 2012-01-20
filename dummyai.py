"""
"	Authors: 	Nicolas Neu & Dennis Zimmermann
"	Date:		20. January 2012
"
"	Rule based AI for Connect6
"
"	Open Issues:
"		- Diagonal Rows
"		- Error in referee 
"""

from sets import Set
from coord import Coord
import random

class DummyAI:
	
	__moves = Set()

	def __init__(self):
		for row in range(19):
			for col in range(19):
				self.__moves.add(Coord(row,col))

	def get_next_move(self, coordstring):
		#I am Player One. Only return one coordinate
		if(coordstring[0:1]=='D'):
			move = random.choice(list(self.__moves))
			self.__moves.discard(move)		
			print move, "jjj"	
			return str(move.get_msg_repr())
		
		#I am Player two, this is my first move. 
		if(coordstring[0:1]=='L'):
			self.__moves.discard(Coord(coordstring[1:3],coordstring[3:5]))	
			self.__moves.discard(Coord(coordstring[5:7],coordstring[7:9]))	
		#Regular Case
		else:
			self.__moves.discard(Coord(coordstring[0:2],coordstring[2:4]))	
			self.__moves.discard(Coord(coordstring[4:6],coordstring[6:8]))	
		
		move1 = random.choice(list(self.__moves))
		self.__moves.discard(move1)
		move2 = random.choice(list(self.__moves))
		self.__moves.discard(move2)		
		

		returnvalue = str(move1.get_msg_repr()+move2.get_msg_repr())
		
		return returnvalue

