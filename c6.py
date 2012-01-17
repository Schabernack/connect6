import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord
from referee import Referee


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
		ref = Referee()
		game = GameBoard()
		game.put_token(Coord(9,9),'B')
		ref.tell_move(Coord(9,9))
		
		m1,m2 = ref.get_next_moves()
		game.put_token(m1,'W')
		game.put_token(m2,'W')
		
		print m1,m2

		game.print_moves()


		start = datetime.datetime.now()
		x = game.get_next_moves('B')
		for b in x:
			b.print_board()
			
		
		print "Time:",datetime.datetime.now()-start
				
	