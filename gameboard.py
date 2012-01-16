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

	def asses(self, player):
		## 1 bei wein, -1 bei lose, 0 bei draw.
		## (anzahl der steine in einer reihe * 2) * anzahl der vorkommen der situation
		## bsp: 2 5er reihen: 2*5 * 2 == 20
		## den den wert minus (dividiert???) durch den wert des gegners.
		## irgendwie auf range(0,1) normalisieren
		pass
