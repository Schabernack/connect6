import itertools
from gameboard import GameBoard 
import datetime
from coord import Coord


class Connect6:

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
		int round = 0
		game = GameBoard()
		game.put_token(Coord(8,8),'B')
		
		game.put_token(Coord(0,1),'W')
		game.put_token(Coord(0,2),'W')
		
		game.put_token(Coord(0,3),'B')
		game.put_token(Coord(0,4),'B')
		
		game.put_token(Coord(0,5),'W')
		game.put_token(Coord(0,6),'W')

		game.print_moves()


		start = datetime.datetime.now()
		x = game.get_next_moves('B')
		for b in x:
			b.print_board()
			break
		
		print "Time:",datetime.datetime.now()-start
				
	