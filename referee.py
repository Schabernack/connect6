import sys
from sets import Set
from coord import Coord

class Referee:
	
	__player = []
	__moves = Set()
	__gameboard = None

	def __init__(self):
		self.__gameboard = [[0]*19 for i in range(19)]

		for row in range(19):
			for col in range(19):
				self.__moves.add(Coord(row,col))

	def add_player(self, player):
		self.__player.append(player)
		if len(self.__player)==2:
			self.start_game()
	
	def put_token(self, coord1, player,  coord2=None):
		color = 'B' if player==0 else 'W'
		if(self.__gameboard[coor1.row][coord1.col]==0):
			self.__gameboard[coord1.row][coord1.col]=color
		else:
			print "Illegal Move by Player ", player
			sys.exit(0)
		
		if coord2 is not None:
			if(self.__gameboard[coor2.row][coord2.col]==0):
				self.__gameboard[coord2.row][coord2.col]=color
			else:
				print "Illegal Move by Player ", player
				sys.exit(0)

		if game_over(player):
			print "Game Over. Player ", player, " won the game. "
			print "Congratulations, you Magnificent Bastard !"
			sys.exit(0)

	def game_over(self):
		return False

		
				

				
	
	def start_game(self):
		player_turn = 0
		# player_move[0] == move of player 0; player_move[1] == move of player 1
		player_move = []

		player_move[0] = self.__player[player_turn].get_next_move('D')
		self.put_token(Coord(player_move[0][0:2], player_move[0][0:2]),0)
		player_move[1] = self.__player[player_turn].get_next_move('L'+player_move[0])
		coords = self.parse_coords(player_move[1]
		self.put_token(coords[0],1, coords[1])

		while (True):
			player_move[player_turn] = self.__player[turn].get_next_move(player_move[switch_player(player_turn)])
			self.put_token(self.parse_coords(player_move[player_turn][0]))
			self.put_token(self.parse_coords(player_move[player_turn][1]))
			player_turn = switch_player(player_turn)

	# 0->1; 1->0
	def switch_player(self, id):
		return (id + 1) % 2
	


	#parses string with len(string)==8; returns 2 coords
	def parse_coords(self, coordstring):
		return Coord(coordstring[0:2],coordstring[2:4]),Coord(coordstring[4:6],coordstring[6:8])


