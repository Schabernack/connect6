from sets import Set
from coord import Coord
import random

class DummyAI:
	
	__moves = Set()

	def __init__(self):
		for row in range(19):
			for col in range(19):
				self.__moves.add(Coord(row,col))

	def get_next_moves(self):
		move1 = random.choice(list(self.__moves))
		self.__moves.discard(move1)
		move2 = random.choice(list(self.__moves))
		self.__moves.discard(move2)

		return move1,move2

	def tell_move(self,coord):
		self.__moves.discard(coord)
