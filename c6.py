import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord



class Player:

	##Todo: Implement alpha-beta pruning
	def minimax(node, depth):
		if depth <= 0:
			return asses(node)
		alpha = -Infinity
		for c in node:
			alpha = max(alpha, -minimax(child, depth-1))
		
		return alpha


	def span_tree_for_node(self,board,depth):
		node = Node(board)
		
		if depth <= 0:
			return node

		for b in board.get_next_moves():
			node.add_child(span_tree_for_node(b,depth-1))

		

	if __name__ == "__main__":
		
		game = GameBoard()
		game.put_token(Coord(9,9),'B')
		game.put_token(Coord(9,14),'B')
		game.put_token(Coord(9,10),'B')
		
		game.drucken()

		


		
			
		
		
				
	