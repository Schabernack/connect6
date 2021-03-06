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

import copy
import os
from sets import Set
import itertools as it
from coord import Coord 
import random

class GameBoard:

	#gezaehlt wird von 1-19
	__board = None


	def __init__(self):
		self.__board = [['']*19 for i in range(19)]
		
	def print_board(self):
		#os.system(['clear','cls'][os.name == 'nt'])
		print"   ",
		for i in range(len(self.__board)):
			print i % 10,
		print
		for col in range(len(self.__board)):
			if col < 10:
				print col," ",
			else:
				print ""+str(col)+" ",
			for row in range(len(self.__board[0])):
				foo = self.__board[row][col]
				if (foo!=''):
					print foo,
				else:
					print ".",
			print ""
			

	def get_copy(self):

		cp_board = GameBoard()
		return cp_board
		
	def put_token(self,coord,player) :
		self.__board[coord.row][coord.col] = player
	
	def get_board(self):
		return self.__board


	