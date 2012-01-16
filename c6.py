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

		
	def build_game_graph(self, board, depth):
		graph = nx.DiGraph
		graph.add_node(board)
		if depth <= 0:
			return graph
		
		for node in get_gametree_children(board, 'B'):
			graph.add_node(node)
			graph.add_edge(board, node)


	def span_tree_for_node(self,board,depth):
		node = Node(board)
		
		if depth <= 0:
			return node

		for b in board.get_next_moves():
			node.add_child(span_tree_for_node(b,depth-1))

		

	if __name__ == "__main__":
		game = GameBoard()
		get_gametree_children(game, 'B')
		game.put_black(3,3)
		game.put_black(3,4)
		game.put_black(3,5)
		game.put_black(3,6)
		print game.asses('B')
		
	