import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord
from sets import Set
# for further explanation of tactic used, see
# Wu, Zhou: Optimization of the Connect6 Classical Evaluation Function
# Based on Threat Theory and Game Strategy (2010)
# http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5708721&tag=1

HOR = 0
VER = 1
DRI = 2
DLE = 3

class Player:
	color = None
	enemy = None
	board = None
	# datastructure (length, [list of free extensions])
	# rows of player
	off_rows = []
	# rows of enemy
	def_rows = []

	
	def __init__(self):
		self.init_boards()


	def init_boards(self):
		self.board = GameBoard()


	def get_next_move(self,message):
		if len(message) == 1:
			self.color = 'D'
			self.enemy = 'L'
			return "1010"
		elif len(message) == 5:
			self.color = 'L'
			self.enemy = 'D'
			coord = Coord(int(message[1:3]),int(message[3:5]))
			self.put_enemy_stones(coord)
		elif len(message) == 8:
			coord1 = Coord(int(message[0:2]),int(message[2:4]))
			coord2 = Coord(int(message[4:6]),int(message[6:8]))
			self.put_enemy_stones(coord1,coord2)

		return self.get_message(self.do_best_move())

	def get_message(self,coord1,coord2):
		msg = ""

		msg += coord1.get_0_prefixed_repr()
		msg += coord2.get_0_prefixed_repr()

		print msg

		return msg
		

	# live 5: just need to put one stone to form a Conn-6,
	# but the opponent need to put two stones to prevent it
	# forming a Conn-6.
	# live 4: need to put two stones to form a Conn-6, also, 
	# two stones is needed to defend.
	# ...
	# returns list of my alive
	def get_alive_off(self, length):
		return filter(lambda live: live[0]==length and self.is_alive(live[1]), self.off_rows)

	#returns a list of opponents alive
	def get_alive_def(self, length):
		return filter(lambda live: live[0]==length and self.is_alive(live[1]), self.def_row)
	
	# similar to Live-5, but only one stone can prevent from Conn-6
	# Sleep-4, similar to Live-4, but only one stone is enough to prevent it.
	# ...
	# returns list of my sleeping
	def get_sleeping_off(self, length):
		return filter(lambda live: live[0]==length and self.is_sleeping(live[1]), self.off_rows)
	
	# returns list of opponents sleeping
	def get_sleeping_def(self, length):
		return filter(lambda live: live[0]==length and self.is_sleeping(live[1]), self.def_rows)
	
	#returns 2 Coords
	def do_best_move(self):
		self.get_rows()
		# if any of our sleep/alive 4/5 exists, make a conn6
		alive5 = self.get_alive_off(5)
		if alive5:
			return self.getCoord(alive5[0][1][0]), self.getCoord(alive5[0][1][1]) 
			
		sleep5 = self.get_sleeping_off(5)
		if sleep5:
			return self.getCoord(sleep5[0][1][0]), self.get_legal_move(1)

		alive4 = self.get_alive_off(4)
		if live4:
			return self.getCoord(alive4[0][1][0]), self.getCoord(alive4[0][1][1])
		
		sleep4 = self.get_sleeping_off(4)
		if sleep4:
			for row in sleep4:
				coord1 = self.getCoord(row[1][0])
				direction = row[2]

				##check if win is possible otherwise check next row
				if (direction == VER):
					if self.board[coord1.row-1][coord1.col]=='':
						return coord1, Coord(coord1.row-1)(coord1.col)
					elif self.board[coord1.row+1][coord1.col]=='':
						return coord1, Coord(coord1.row+1)(coord1.col)
				elif (direction == HOR):
					if self.board[coord1.row][coord1.col-1]=='':
						return coord1, Coord(coord1.row)(coord1.col-1)
					elif self.board[coord1.row][coord1.col+1]=='':
						return coord1, Coord(coord1.row)(coord1.col+1)
				elif (direction == DRI):
					if self.board[coord1.row-1][coord1.col-1]=='':
						return coord1, Coord(coord1.row-1)(coord1.col-1)
					elif self.board[coord1.row+1][coord1.col+1]=='':
						return coord1, Coord(coord1.row+1)(coord1.col+1)
				else:
					if self.board[coord1.row-1][coord1.col+1]=='':
						return coord1, Coord(coord1.row-1)(coord1.col+1)
					elif self.board[coord1.row+1][coord1.col-1]=='':
						return coord1, Coord(coord1.row+1)(coord1.col-1)

		
		# if enemy has sleep/alive 4/5 exists, make it dead
		alive5 = self.get_alive_def(5)
		if alive5:
			return self.getCoord(alive5[0][1][0]), self.getCoord(alive5[0][1][1])
		
		alive4 = self.get_alive_def(4)
		if alive4:
			return self.getCoord(sleep4[0][1][0]), self.getCoord(alive4[0][1][1])


		sleep5 = self.get_sleeping_def(5)
		if sleep5:
			# If only one sleep 5? improve own standing, else: destroy other sleep5
			if len(sleep5) == 1:
				return self.getCoord(sleep5[0][1][0]), self.get_improvement_move(1)
			else:
				return self.getCoord(sleep5[0][1][0]), self.getCoord(sleep5[1][1][0])
		
		## toDo only put to sleep if conn-6 is possible

		sleep4 = self.get_sleeping_def(4)
		if sleep4:
			if len(sleep4) == 1:
				return self.getCoord(sleep4[0][1][0]), self.get_improvement_move(1)
			else:
				return self.getCoord(sleep4[0][1][0]), self.getCoord(sleep4[1][1][0])
		
		return self.get_improvement_move(2)


	## Avoided opponent win .. do best move
	## Put enemy live2/3 to sleep
	## ...
	def get_improvement_move(self,count):
		#
		alive3 = self.get_alive_def(3)
		if alive3:
			if len(alive3) == 1: 
				if count == 2:
					return self.getCoord(alive3[0][1][0]), self.do_offensive_move(1)
				else: 
					return self.getCoord(alive3[0][1][0])
			else:
				if count == 2:
					return self.getCoord(alive3[0][1][0]), self.getCoord(alive3[1][1][0])
				else:
					return self.getCoord(alive3[0][1][0])
		
		alive2 = self.get_alive_def(2)
		if alive2:
			if len(alive2) == 1: 
				if count == 2:
					return self.getCoord(alive2[0][1][0]), self.do_offensive_move(1)
				else: 
					return self.getCoord(alive2[0][1][0])
			else:
				if count == 2:
					return self.getCoord(alive2[0][1][0]), self.getCoord(alive2[1][1][0])
				else:
					return self.getCoord(alive2[0][1][0])

		return self.do_offensive_move(2)

	## enemy live2/3 were put to sleep
	## remaining moves for offense

	def get_offensive_move(self,count):
		returnCount = count
		moves = []
		while (count > 0):
			alive3 = self.get_alive_off(3)

			for row in alive3:
				coord1 = self.getCoord(row[1][0])
				direction = row[2]

				##check if win is possible otherwise check next row
				if (direction == VER):
					if self.board[coord1.row-1][coord1.col]=='':
						moves.append(coord1)
						count -= 1
					elif self.board[coord1.row+1][coord1.col]=='':
						moves.append(coord1)
						count -= 1
				elif (direction == HOR):
					if self.board[coord1.row][coord1.col-1]=='':
						moves.append(coord1)
						count -= 1
					elif self.board[coord1.row][coord1.col+1]=='':
						moves.append(coord1)
						count -= 1
				elif (direction == DRI):
					if self.board[coord1.row-1][coord1.col-1]=='':
						moves.append(coord1)
						count -= 1
					elif self.board[coord1.row+1][coord1.col+1]=='':
						moves.append(coord1)
						count -= 1
				else:
					if self.board[coord1.row-1][coord1.col+1]=='':
						moves.append(coord1)
						count -= 1
					elif self.board[coord1.row+1][coord1.col-1]=='':
						moves.append(coord1)
						count -= 1
			if (count > 0):	
				alive2 = self.get_alive_off(2)

				for row in alive2:
					coord1 = self.getCoord(row[1][0])
					direction = row[2]

					##check if win is possible otherwise check next row
					if (direction == VER):
						if self.board[coord1.row-1][coord1.col]=='':
							moves.append(coord1)
							count -= 1
						elif self.board[coord1.row+1][coord1.col]=='':
							moves.append(coord1)
							count -= 1
					elif (direction == HOR):
						if self.board[coord1.row][coord1.col-1]=='':
							moves.append(coord1)
							count -= 1
						elif self.board[coord1.row][coord1.col+1]=='':
							moves.append(coord1)
							count -= 1
					elif (direction == DRI):
						if self.board[coord1.row-1][coord1.col-1]=='':
							moves.append(coord1)
							count -= 1
						elif self.board[coord1.row+1][coord1.col+1]=='':
							moves.append(coord1)
							count -= 1
					else:
						if self.board[coord1.row-1][coord1.col+1]=='':
							moves.append(coord1)
							count -= 1
						elif self.board[coord1.row+1][coord1.col-1]=='':
							moves.append(coord1)
							count -= 1
				if (count > 0):
					alive1 = self.get_alive_off(1)
					for row in alive1:
						coord1 = self.getCoord(row[1][0])
						moves.append(coord1)
						count -= 1
					
					if (count > 0):	
						sleep1 = self.get_sleeping_off(2)

						for row in sleep1:
							coord1 = self.getCoord(row[1][0])
							direction = row[2]

							##check if win is possible otherwise check next row
							if (direction == VER):
								if self.board[coord1.row-1][coord1.col]=='':
									moves.append(coord1)
									count -= 1
								elif self.board[coord1.row+1][coord1.col]=='':
									moves.append(coord1)
									count -= 1
							elif (direction == HOR):
								if self.board[coord1.row][coord1.col-1]=='':
									moves.append(coord1)
									count -= 1
								elif self.board[coord1.row][coord1.col+1]=='':
									moves.append(coord1)
									count -= 1
							elif (direction == DRI):
								if self.board[coord1.row-1][coord1.col-1]=='':
									moves.append(coord1)
									count -= 1
								elif self.board[coord1.row+1][coord1.col+1]=='':
									moves.append(coord1)
									count -= 1
							else:
								if self.board[coord1.row-1][coord1.col+1]=='':
									moves.append(coord1)
									count -= 1
								elif self.board[coord1.row+1][coord1.col-1]=='':
									moves.append(coord1)
									count -= 1
						if (count > 0):
							moves.append(self.get_legal_move(count))

		if returnMoves == 1:
			return moves[0]
		elif returnMoves == 2:
			return moves[0],moves[1]

		

	def get_legal_move(self,count):
		freecoord = []
		should_i_break_or_should_i_go=False
		for r in range(len(self.board)):
			for c in range(len(self.board[0])):
				if self.board[r][c]=='':
					freecoord.append(Coord(r,c))
					if (len(freecoord)==count):
						should_i_break_or_should_i_go=True
						break
			if should_i_break_or_should_i_go:
				break
		if count==1:
			return freecoord[0]
		elif count==2:
			return freecoord[0],freecoord[1]

	
	def getCoord(self,tuple):
		return Coord(tuple[0],tuple[1])

	def put_enemy_stones(self,coord1,coord2=None):
		self.board.put_token(coord1,self.enemy)
		if coord2 != None:
			self.board.put_token(coord2,self.enemy)
	

	def get_rows(self):
		self.get_horizontal_rows()
		self.get_vertical_rows()

	def get_horizontal_rows(self):
		
		previous_color = ''

		off_row = None
		def_row = None

		for r in range(19):
			for c in range(19):
				token = self.board.get_board()[r][c]
			
				## player field
				if token == self.color:
					## Extend self.player row
					if previous_color == self.color:
						off_row = (off_row[0]+1,off_row[1],HOR)
					## New self.player row
					else:
						## self.enemy_row disturbed?
						if def_row != None:
							self.def_rows.append(def_row)
							def_row = None

						off_row = (1,[],HOR)

						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r][c-1] == '':
								off_row = (off_row[0],[(r,c-1)],HOR)
			

				## enemy field
				elif token == self.enemy:
					## Extend self.enemy row
					if previous_color == self.enemy:
						def_row = (def_row[0]+1,def_row[1],HOR)
					## New self.enemy row
					else:
						## self.player row disturbed?
						if off_row != None:
							self.off_rows.append(off_row)
							off_row = None
						
						def_row = (1,[],HOR)
						
						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r][c-1] == '':
								def_row = (def_row[0],[(r,c-1)],HOR)
						
						
				## Free field
				else:
					## Any rows disturbed?
					if off_row != None:
							off_row[1].append((r,c))
							self.off_rows.append(off_row)
							off_row = None
					if def_row != None:
							def_row[1].append((r,c))
							self.def_rows.append(def_row)
							def_row = None

				
				previous_color = token

	def get_vertical_rows(self):
		
		previous_color = ''

		off_row = None
		def_row = None

		for c in range(19):
			for r in range(19):
				token = self.board.get_board()[r][c]

				## player field
				if token == self.color:
					## Extend self.player row
					if previous_color == self.color:
						off_row = (off_row[0]+1,off_row[1],VER)
					## New self.player row
					else:
						## self.enemy_row disturbed?
						if def_row != None:
							self.def_rows.append(def_row)
							def_row = None

						off_row = (1,[])

						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r-1][c] == '':
								off_row = (off_row[0],[(r-1,c)],VER)
			

				## enemy field
				elif token == self.enemy:
					## Extend self.enemy row
					if previous_color == self.enemy:
						def_row = (def_row[0]+1,def_row[1])
					## New self.enemy row
					else:
						## self.player row disturbed?
						if off_row != None:
							self.off_rows.append(off_row)
							off_row = None
						
						def_row = (1,[],VER)
						
						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r-1][c] == '':
								def_row = (def_row[0],[(r-1,c)],VER)
						
						
				## Free field
				else:
					## Any rows disturbed?
					if off_row != None:
							off_row[1].append((r,c))
							self.off_rows.append(off_row)
							off_row = None
					if def_row != None:
							def_row[1].append((r,c))
							self.def_rows.append(def_row)
							def_row = None

				
				previous_color = token


	def is_alive(self,row):
		return True if len(row[1]) > 1 else False

	def is_dead(self,row):
		return True if len(row[1]) == 0 else False

	def is_sleeping(self,row):
		return True if len(row[1]) == 1 else False
					
	def get_enemy_rows(self):
		return sorted(self.def_rows, key=lambda number:(number[0], len(number[1])),reverse=True)

	def get_player_rows(self):
		return sorted(self.off_rows, key=lambda number:(number[0], len(number[1])),reverse=True)
	


		

				
	