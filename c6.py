import networkx as nx
import itertools
from gameboard import GameBoard 

class MinMax:

	##Todo: Implement alpha-beta pruning
	def minimax(node, depth):
		if depth <= 0:
			return asses(node)
		alpha = -Infinity
		for c in node:
			alpha = max(alpha, -minimax(child, depth-1))
		
		return alpha
	
	#params: gamesituation a c6 board
	#returns a list gamesituations
	def get_gametree_children(gamesituation, color):
		game = GameBoard()
		graph = nx.DiGraph()
		gamelist = []
		coordinates = []
		for row in range(18):
			for col in range(17):
				board = gamesituation.get_copy()
				if  not board.get_board()[row][col] and not board.get_board()[row][col+1]:
					board.get_board()[row][col]=color
		for row in range(18):
			for col in range(18):
				coordinates.append((row,col))
		
		coordinate_tuple = it.product(coordinates, coordinates)
		for ctuple in coordinate_tuple:
			if  not board.get_board()[ctuple[0][0]][ctuple[0][1]] and not board.get_board()[ctuple[1][0]][ctuple[1][1]]:		
				board = gamesituation.get_copy()
				if color=='B':
					board.put_black(ctuple[0][0],[ctuple[0][1])
					board.put_black(ctuple[1][0],[ctuple[1][1])
				else:
					board.put_white(ctuple[0][0],[ctuple[0][1])
					board.put_white(ctuple[1][0],[ctuple[1][1])
			gamelist.append(board)
			
		return gamelist
		
	def build_game_graph(self, board, depth):
		graph = nx.DiGraph
		graph.add_node(board)
		if depth <= 0:
			return graph
		
		for node in get_gametree_children(board, 'B'):
			graph.add_node(node)
			graph.add_edge(board, node)

		

	if __name__ == "__main__":
		game = GameBoard()
		get_gametree_children(game, 'B')
		game.put_black(3,3)
		game.put_black(3,4)
		game.put_black(3,5)
		game.put_black(3,6)
		print game.asses('B')
		
	