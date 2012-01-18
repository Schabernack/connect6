import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord
from referee import Referee
from node import Node


class Player:
	color = None
	enemy = None
	game_board = None
	hor_off_board = None
	hor_off_rows = []
	ver_off_board = None
	ver_off_rows = []

	dle_off_board = None
	dle_off_rows = []

	dri_off_board = None
	dri_off_rows = []


	hor_def_board = None
	hor_def_rows = []	

	ver_def_board = None
	ver_def_rows = []

	dle_def_board = None
	dle_def_rows = []

	dri_def_board = None
	dri_def_rows = []

	def __init__(self):
		self.init_boards()


	def init_boards(self):
		self.game_board = GameBoard()
		self.hor_off_board = [[0]*19 for i in range(19)]
		self.ver_off_board = [[0]*19 for i in range(19)]
		self.dle_off_board = [[0]*19 for i in range(19)]
		self.dri_off_board = [[0]*19 for i in range(19)]
		
		self.hor_def_board = [[0]*19 for i in range(19)]
		self.ver_def_board = [[0]*19 for i in range(19)]
		self.dle_def_board = [[0]*19 for i in range(19)]
		self.dri_def_board = [[0]*19 for i in range(19)]


	def get_next_move(self,message):
		if len(message) == 1:
			self.color = 'D'
			self.enemy = 'L'
		elif len(message) == 5:
			self.color = 'L'
			self.enemy = 'D'
			coord = (int(message[1:3]),int(message[3:5])
			self.put_enemy_stones(coord)
		elif len(message) == 8:
			coord1 = int(message[0:2]),int(message[2:4]
			coord2 = int(message[4:6]),int(message[6:8]
			self.put_enemy_stones(coord1,coord2)
		
		return do_best_move()


	def do_best_move():
		move = ""

		self.adjust_off_board(move)

		return move


	def put_enemy_stones(coord1,coord2=None):
		game_board.put_token(enemy,coord1)
		if coord2 != None:
			game_board.put_token(enemy,coord2)

		self.adjust_def_boards(coord1,coord2)

	
	def adjust_def_boards(coord1,coord2=None):
		coords = []
		coords.append(coord1)
		if coord2 != None:
			coords.append(coord2)

		for coord in coords:
			up = hor_def_board[coord.row+1][coord.col] 		if coord.row+1 < 19		else 0
			down = hor_def_board[coord.row-1][coord.col]	if coord.row-1 >= 0 	else 0
			hor_def_board[coord.row][coord.col] = up+down+1
			
			left = hor_def_board[coord.row][coord.col-1]		if coord.col-1 >= 0 	else 0
			right = hor_def_board[coord.row][coord.col+1]		if coord.col+1 < 19 	else 0
			ver_def_board[coord.row][coord.col] = left+right+1

			up_left = hor_def_board[coord.row+1][coord.col-1]			if coord.row+1 < 19 and coord.col-1 >= 0 	else 0
			down_right = hor_def_board[coord.row-1][coord.col+1]		if coord.row-1 >= 0 and coord.col+1 < 19 	else 0
			dri_def_board[coord.row][coord.col] = up_left+up_right+1
			
			up_right = hor_def_board[coord.row+1][coord.col+1]			if coord.row+1 < 19 and coord.col+1 < 19 	else 0
			down_left = hor_def_board[coord.row-1][coord.col-1]			if coord.row-1 >= 0 and coord.col-1 >= 0 	else 0
			dle_def_board[coord.row][coord.col] = up_right+down_left+1


	def adjust_off_boards(coord1,coord2=None):
		coords = []
		coords.append(coord1)
		if coord2 != None:
			coords.append(coord2)

		for coord in coords:
			up = hor_off_board[coord.row+1][coord.col] 		if coord.row+1 < 19		else 0
			down = hor_off_board[coord.row-1][coord.col]	if coord.row-1 >= 0 	else 0
			hor_off_board[coord.row][coord.col] = 1
			
			left = hor_off_board[coord.row][coord.col-1]		if coord.col-1 >= 0 	else 0
			right = hor_off_board[coord.row][coord.col+1]		if coord.col+1 < 19 	else 0
			ver_off_board[coord.row][coord.col] = 1

			up_left = hor_off_board[coord.row+1][coord.col-1]			if coord.row+1 < 19 and coord.col-1 >= 0 	else 0
			down_right = hor_off_board[coord.row-1][coord.col+1]		if coord.row-1 >= 0 and coord.col+1 < 19 	else 0
			dri_off_board[coord.row][coord.col] = 1
			
			up_right = hor_off_board[coord.row+1][coord.col+1]			if coord.row+1 < 19 and coord.col+1 < 19 	else 0
			down_left = hor_off_board[coord.row-1][coord.col-1]			if coord.row-1 >= 0 and coord.col-1 >= 0 	else 0
			dle_off_board[coord.row][coord.col] = 1
			
		hor_count = 0
		ver_count = 0
		dle_count = 0
		dri_count = 0

		for col in range(19):
			for row in range(19):
				r = hor_off_board[row][col]
				if r = 0:
					break
				else:
					hor_count += 1



		


	

		

				
	