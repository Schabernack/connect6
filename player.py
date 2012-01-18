import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord
from sets import Set


class Player:
	color = None
	enemy = None
	board = None
	off_rows = []
	def_rows = []

	def __init__(self):
		self.init_boards()


	def init_boards(self):
		self.board = GameBoard()


	def get_next_move(self,message):
		if len(message) == 1:
			self.color = 'D'
			self.enemy = 'L'
		elif len(message) == 5:
			self.color = 'L'
			self.enemy = 'D'
			coord = Coord(int(message[1:3]),int(message[3:5]))
			self.put_enemy_stones(coord)
		elif len(message) == 8:
			coord1 = Coord(int(message[0:2]),int(message[2:4]))
			coord2 = Coord(int(message[4:6]),int(message[6:8]))
			self.put_enemy_stones(coord1,coord2)

		self.board.put_token(Coord(1,1),self.color)

		


	def do_best_move(self):
		move = ""

		return move


	def put_enemy_stones(self,coord1,coord2=None):
		self.board.put_token(coord1,self.enemy)
		if coord2 != None:
			self.board.put_token(coord2,self.enemy)
	

'''
'''
'''			CHECK OTHER FREE FIELDS FOR VERTICAL ROWS!!!
'''
'''
'''

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
						off_row = (off_row[0]+1,off_row[1])
					## New self.player row
					else:
						## self.enemy_row disturbed?
						if def_row != None:
							self.def_rows.append(def_row)
							def_row = None

						off_row = (1,[])

						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r][c-1] == '':
								off_row = (off_row[0],[(r,c-1)])
			

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
						
						def_row = (1,[])
						
						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r][c-1] == '':
								def_row = (def_row[0],[(r,c-1)])
						
						
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
						off_row = (off_row[0]+1,off_row[1])
					## New self.player row
					else:
						## self.enemy_row disturbed?
						if def_row != None:
							self.def_rows.append(def_row)
							def_row = None

						off_row = (1,[])

						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r][c-1] == '':
								off_row = (off_row[0],[(r,c-1)])
			

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
						
						def_row = (1,[])
						
						## Check if previous field is free
						if c > 0:
							if self.board.get_board()[r][c-1] == '':
								def_row = (def_row[0],[(r,c-1)])
						
						
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
	
if __name__ == "__main__":
	
	player = Player()
	player.get_next_move("L0000")

	player.get_horizontal_rows()
	player.get_vertical_rows()

	player.get_enemy_rows()

	player.board.print_board()

	print "Enemy"
	for row in player.get_enemy_rows():
		print row

	print "Me"
	for row in player.get_player_rows():
		print row
	

	


	

		

				
	