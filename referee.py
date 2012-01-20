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

import time
import sys
from sets import Set
from coord import Coord
from gameboard import GameBoard

class Referee:
	
	__player = []
	__gameboard = None
	__moves = []

	def __init__(self):
		self.__gameboard = GameBoard()

		

	def add_player(self, player):
		self.__player.append(player)
		if len(self.__player)==2:
			print "Go!"
			self.start_game()
	
	def put_token(self, coord1, player,  coord2=None):
		color = 'B' if player==0 else 'W'
		print "Coords:",coord1,coord2
		
		if self.__gameboard.get_board()[coord1.row][coord1.col] == '':
			self.__gameboard.get_board()[coord1.row][coord1.col]=color
		else:
			print "Illegal Move by Player ", player, " ", coord1, coord2
			print "@",coord1.row,coord1.col,self.__gameboard.get_board()[coord1.row][coord1.col]
			self.__gameboard.print_board()
			sys.exit(0)
		
		if coord2 is not None:
			if self.__gameboard.get_board()[coord2.row][coord2.col]=='':
				self.__gameboard.get_board()[coord2.row][coord2.col]=color
			else:

				print "Illegal Move by Player ", player, " ", coord1, coord2
				print "@",coord2.row,coord2.col,self.__gameboard.get_board()[coord2.row][coord2.col]
				self.__gameboard.print_board()
				sys.exit(0)

		if self.game_over():
			print "Game Over. Player ", player, " won the game. "
			print "Congratulations, you Magnificent Bastard !"
			sys.exit(0)

	def game_over2(self):
		for row in range(len(self.__gameboard.get_board())):
			for col in range(len(self.__gameboard.get_board()[0])):
				foo= self.__gameboard.get_board()[row][col]
				if foo == '':
					break
				try:
					#check horizontal
					foo= self.__gameboard.get_board()[row][col]
					for i in range(6):
						if(foo!=self.__gameboard.get_board()[row][col+i]):
							break
						elif i==5:
							return True
						foo= self.__gameboard.get_board()[row][col+i]

					#check vertical
					foo= self.__gameboard.get_board()[row][col]
					for i in range(6):
						if(foo!=self.__gameboard.get_board()[row+i][col]):
							break
						elif i==5:
							return True
						foo= self.__gameboard.get_board()[row+i][col]
					
					#check diagonal up left 
					foo= self.__gameboard.get_board()[row][col]
					for i in range(6):
						if(foo!=self.__gameboard.get_board()[row-i][col+i]):
							break
						elif i==5:
							print "li74"
							return True
						foo= self.__gameboard.get_board()[row-i][col+i]

					#check diagonal down right
					foo = self.__gameboard.get_board()[row][col]
					for i in range(6):
						if(foo!=self.__gameboard.get_board()[row+i][col-i]):
							break
						else:
							foo = self.__gameboard.get_board()[row+i][col-i]	
				
				except:
					# Don't care. Never Did. Never Will.
					pass

				return False


	def game_over(self):
		p1 = 'B'
		p2 = 'W'
		previous_color = ''
		p1_rows = []
		p2_rows = []
		p1_row = None
		p2_row = None

		for c in range(19):
			for r in range(19):
				token = self.__gameboard.get_board()[c][r]
				## player field
				if token == p1:
					## Extend self.player row
					if previous_color == p1:
						p1_row += 1
						if p1_row == 6:
							print "Player B wins!"
							sys.exit()
					## New self.player row
					else:
						## p2_row disturbed?
						if p2_row != None:
							p2_rows.append(p2_row)
							p2_row = None
						p1_row = 1

				## enemy field
				elif token == p2:
					## Extend p2 row
					if previous_color == p2:
						p2_row += 1
						if p2_row == 6:
							print "Player W wins!"
							sys.exit()
					## New p2 row
					else:
						## self.player row disturbed?
						if p1_row != None:
							p1_rows.append(p1_row)
							p1_row = None
						
						p2_row = 1
						
				## Free field
				else:
					## Any rows disturbed?
					if p1_row != None:
						p1_rows.append(p1_row)
						p1_row = None
					if p2_row != None:
						p2_rows.append(p2_row)
						p2_row = None

				
				previous_color = token

		for r in range(19):
			for c in range(19):
				token = self.__gameboard.get_board()[r][c]
				## player field
				if token == p1:
					## Extend self.player row
					if previous_color == p1:
						p1_row += 1
						if p1_row == 6:
							print "Player B wins!"
							sys.exit()
					## New self.player row
					else:
						## p2_row disturbed?
						if p2_row != None:
							p2_rows.append(p2_row)
							p2_row = None
						p1_row = 1

				## enemy field
				elif token == p2:
					## Extend p2 row
					if previous_color == p2:
						p2_row += 1
						if p2_row == 6:
							print "Player W wins!"
							sys.exit()
					## New p2 row
					else:
						## self.player row disturbed?
						if p1_row != None:
							p1_rows.append(p1_row)
							p1_row = None
						
						p2_row = 1
						
				## Free field
				else:
					## Any rows disturbed?
					if p1_row != None:
						p1_rows.append(p1_row)
						p1_row = None
					if p2_row != None:
						p2_rows.append(p2_row)
						p2_row = None

				
				previous_color = token

		
	

				
	# walk that walk, talk that talk, play that game!
	def start_game(self):

		player_turn = 0
		# player_move[0] == move of player 0; player_move[1] == move of player 1
		player_move = [None]*2

		player_move[0] = (self.__player[player_turn].get_next_move('D'))
		if(player_move[0] and len(player_move[0])>4):
			print "Illegal Move by Player 0 (Two tokens as first move)"
			sys.exit(0)
		print "Player B: ", player_move[0]
		self.put_token(Coord(int(player_move[0][0:2]),int(player_move[0][2:4])),0)
		self.__gameboard.print_board()

		player_turn = self.switch_player(player_turn)


		player_move[1] = self.__player[player_turn].get_next_move('L'+player_move[0])
		print "Player W: ", player_move[1]
		coords = self.parse_coords(player_move[1])
		print coords
		self.put_token(coords[0],1, coords[1])
		self.__gameboard.print_board()

		player_turn = self.switch_player(player_turn)

		while (True):
			starttime = self.milliseconds()
			player_move[player_turn] = self.__player[player_turn].get_next_move(player_move[self.switch_player(player_turn)])
			print "Recieved:",player_move[player_turn]
			self.put_token(self.parse_coords(player_move[player_turn])[0], player_turn,self.parse_coords(player_move[player_turn])[1])
			stoptime = self.milliseconds()
			#if stoptime - starttime < 2000:
			#	sleeptime = 2000 - stoptime-starttime
			time.sleep(0.3)
			self.__gameboard.print_board()
			player_turn = self.switch_player(player_turn)

	# 0->1; 1->0
	def switch_player(self, id):
		return (id + 1) % 2
	
	def milliseconds(self):
		return int(round(time.time() * 1000))

	#parses string with len(string)==8; returns 2 coords
	def parse_coords(self, coordstring):
		return  Coord(int(coordstring[0:2]),int(coordstring[2:4])), Coord(int(coordstring[4:6]),int(coordstring[6:8]))


