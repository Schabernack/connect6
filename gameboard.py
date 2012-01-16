import pprint 
import copy

class GameBoard:

	#gezaehlt wird von 1-19
	__board = None

	def __init__(self, board=[[0]*18 for i in range(18)]):
		self.__board = board

	def get_copy(self):
		boardlist = copy.deepcopy(self.__board)
		foo = GameBoard(boardlist)
		return foo
		
	

	def put_black(self,row, column) :
		self.__board[row-1][column-1]= 'B'

	def put_white(self,row,column):
		self.__board[row-1][column-1]= 'W'
	
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

		return goodvalue -  badvalue

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
	def get_next_moves(color):
		board = __board.get_copy()
		gamelist = []
		coordinates = []

		for row in range(18):
			for col in range(18):
				coordinates.append((row,col))
		
		coordinate_tuple = it.product(coordinates, coordinates)
		for ctuple in coordinate_tuple:
			if  not board.get_board()[ctuple[0][0]][ctuple[0][1]] and not board.get_board()[ctuple[1][0]][ctuple[1][1]]:		
				board = gamesituation.get_copy()
				if color=='B':
					board.put_black(ctuple[0][0],ctuple[0][1])
					board.put_black(ctuple[1][0],ctuple[1][1])
				else:
					board.put_white(ctuple[0][0],ctuple[0][1])
					board.put_white(ctuple[1][0],ctuple[1][1])
			gamelist.append(board)
			
		return gamelist
