import pprint 
import copy
from sets import Set
import itertools as it
from coord import Coord 
import random

class GameBoard:

	#gezaehlt wird von 1-19
	__board = None


	def __init__(self):
		self.__board = [['']*19 for i in range(19)]
		

	def get_copy(self):

		cp_board = GameBoard()
		return cp_board
		
	def put_token(self,coord,player) :
		self.__board[coord.row][coord.col] = player
	
	def get_board(self):
		return self.__board

	def print_board(self):
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(self.__board)


	