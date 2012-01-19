import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord
from sets import Set

# for further explanation of tactic used, see
# Wu, Zhou: Optimization of the Connect6 Classical Evaluation Function
# Based on Threat Theory and Game Strategy (2010)
# http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5708721&tag=1


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

	# live 5: just need to put one stone to form a Conn-6,
	# but the opponent need to put two stones to prevent it
	# forming a Conn-6.
	# live 4: need to put two stones to form a Conn-6, also, 
	# two stones is needed to defend.
	# ...
	# returns list of alive
	def get_alive(self, length):
		return filter(lambda live: live[0]==length and self.is_alive(live[1]), self.off_rows)
	
	# similar to Live-5, but only one stone can prevent from Conn-6
	# Sleep-4, similar to Live-4, but only one stone is enough to prevent it.
	# ...
	# returns list of sleeping
	def get_sleeping(self, length):
		return filter(lambda live: live[0]==length and self.is_sleeping(live[1]), self.off_rows)

	def do_best_move(self):
		move = ""

		return move


	def put_enemy_stones(self,coord1,coord2=None):
		self.board.put_token(coord1,self.enemy)
		if coord2 != None:
			self.board.put_token(coord2,self.enemy)
	

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
							if self.board.get_board()[r-1][c] == '':
								off_row = (off_row[0],[(r-1,c)])
			

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
							if self.board.get_board()[r-1][c] == '':
								def_row = (def_row[0],[(r-1,c)])
						
						
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

	print player.get_alive(2)
	

	


	

		

				
	