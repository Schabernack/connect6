import pprint 
import copy
from sets import Set
import itertools as it
from coord import Coord as Coord

class GameBoard:

	#gezaehlt wird von 1-19
	__board = None

	__moves = Set()
	__taken = Set()


	def __init__(self):
		self.__board = [[0]*19 for i in range(19)]
		

	def get_copy(self):
		boardlist = copy.deepcopy(self.__board)
		movelist = copy.deepcopy(self.__moves)

		cp_board = GameBoard()
		cp_board.__board = boardlist
		cp_board.__moves = movelist
		return cp_board
		
	def put_token(self,coord,player) :
		self.__board[coord.row][coord.col] = player
		self.__taken.add(coord)
		possible_moves = self.get_nearest_cells(coord)

		self.__moves = self.__moves.union(possible_moves)
		self.__moves = self.__moves.difference(self.__taken)


	def print_moves(self):
		print self.__moves
		print len(self.__moves)
	
	def get_board(self):
		return self.__board

	def print_board(self):
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(self.__board)

	def asses(self, color):
		## 1 bei win, -1 bei lose, 0 bei draw?
		## (anzahl der steine in einer reihe * 2) * anzahl der vorkommen der situation
		## bsp: 2 5er reihen: 2*5 * 2 == 20
		## den den wert minus (dividiert???) durch den wert des gegners.
		## irgendwie auf range(0,1) normalisieren?
		mycolor = color
		enemycolor = 'B' if mycolor == 'W' else 'W'
		goodvalue = 0
		for i in range(2,6):
			goodvalue += self.how_many_vlines(mycolor)[str(i)]* 2 * i
			goodvalue += self.how_many_hlines(mycolor)[str(i)]* 2 * i
			goodvalue += self.how_many_drlines(mycolor)[str(i)]* 2 * i
			goodvalue += self.how_many_dllines(mycolor)[str(i)]* 2 * i
		badvalue = 0
		for i in range(2,6):
			badvalue += self.how_many_vlines(enemycolor)[str(i)]* 2 * i
			badvalue += self.how_many_hlines(enemycolor)[str(i)]* 2 * i
			badvalue += self.how_many_drlines(enemycolor)[str(i)]* 2 * i
			badvalue += self.how_many_dllines(enemycolor)[str(i)]* 2 * i

		return goodvalue - badvalue

	def how_many_vlines(self, color):
		resultlist = {'2':0, '3':0, '4':0, '5':0}
		for row in range(len(self.__board)):
			for col in range(len(self.__board[row])):
				try:
					if(self.__board[row][col]==self.__board[row][col+1]==color):
						resultlist['2']+=1
					if(self.__board[row][col]==self.__board[row][col+1]==self.__board[row][col+2]==color):
						resultlist['3']+=1
					if(self.__board[row][col]==self.__board[row][col+1]==self.__board[row][col+2]==self.__board[row][col+3]==color):
						resultlist['4']+=1
					if(self.__board[row][col]==self.__board[row][col+1]==self.__board[row][col+2]==self.__board[row][col+3]==self.__board[row][col+4]==color):
						resultlist['5']+=1
				except:
					# real men dont need error handling.
					pass

		return resultlist

	def how_many_hlines(self, color):
		resultlist = {'2':0, '3':0, '4':0, '5':0}
		for row in range(len(self.__board)):
			for col in range(len(self.__board[row])):
				try:
					if(self.__board[row][col]==self.__board[row+1][col]==color):
						resultlist['2']+=1
					if(self.__board[row][col]==self.__board[row+1][col]==self.__board[row+2][col]==color):
						resultlist['3']+=1
					if(self.__board[row][col]==self.__board[row+1][col]==self.__board[row+2][col]==self.__board[row+3][col]==color):
						resultlist['4']+=1
					if(self.__board[row][col]==self.__board[row+1][col]==self.__board[row+2][col]==self.__board[row+3][col]==self.__board[row+4][col]==color):
						resultlist['5']+=1
				except:
					pass
		return resultlist

	#diagonal lines: up left to down right
	def how_many_drlines(self, color):
		resultlist = {'2':0, '3':0, '4':0, '5':0}
		for row in range(len(self.__board)):
			for col in range(len(self.__board[row])):
				try:
					if(self.__board[row][col]==self.__board[row+1][col+1]==color):
						resultlist['2']+=1
					if(self.__board[row][col]==self.__board[row+1][col+1]==self.__board[row+2][col+2]==color):
						resultlist['3']+=1
					if(self.__board[row][col]==self.__board[row+1][col+1]==self.__board[row+2][col+2]==self.__board[row+3][col+3]==color):
						resultlist['4']+=1
					if(self.__board[row][col]==self.__board[row+1][col]==self.__board[row+2][col+2]==self.__board[row+3][col+3]==self.__board[row+4][col+4]==color):
						resultlist['5']+=1
				except:
					pass
		
		return resultlist

	#diagonal lines: up right to down left
	def how_many_dllines(self, color):
		resultlist = {'2':0, '3':0, '4':0, '5':0}
		for row in range(len(self.__board)):
			for col in range(len(self.__board[row])):
				try:
					if(self.__board[row][col]==self.__board[row-1][col-1]==color):
						resultlist['2']+=1
					if(self.__board[row][col]==self.__board[row-1][col-1]==self.__board[row-2][col-2]==color):
						resultlist['3']+=1
					if(self.__board[row][col]==self.__board[row-1][col-1]==self.__board[row-2][col-2]==self.__board[row-3][col-3]==color):
						resultlist['4']+=1
					if(self.__board[row][col]==self.__board[row+1][col]==self.__board[row-2][col-2]==self.__board[row-3][col-3]==self.__board[row-4][col-4]==color):
						resultlist['5']+=1
				except:
					pass
		
		return resultlist

	#params: gamesituation a c6 board
	#returns a list gamesituations
	def get_next_moves(self,color):
		gamelist = []
		
		coordinate_tuple = self.get_possible_moves()
		for ctuple in coordinate_tuple:
			board = self.get_copy()
			board.put_token(ctuple[0],color)
			board.put_token(ctuple[1],color)
			
			gamelist.append(board)
			
		return gamelist

	## returns possible move-tuples
	def get_possible_moves(self):
		p_moves = Set()
		move_list=list(self.__moves)
		for i in range(len(self.__moves)):
			for j in range(len(self.__moves)):
				if i!=j+i and i+j < len(move_list):
					p_moves.add((move_list[i],move_list[i+j]))
		return p_moves



	def get_nearest_cells(self,c,radius=2):
		cells = Set()
		for dist in range(1,radius+1):

			## diagonal neighbours
			cells.add(Coord(c.row+dist,c.col+dist))
			cells.add(Coord(c.row+dist,c.col-dist))
			cells.add(Coord(c.row-dist,c.col+dist))
			cells.add(Coord(c.row-dist,c.col-dist))
			
			## direct neighbours
			cells.add(Coord(c.row+dist,c.col))
			cells.add(Coord(c.row-dist,c.col))
			cells.add(Coord(c.row,c.col+dist))
			cells.add(Coord(c.row,c.col-dist))
		
		return cells
				













