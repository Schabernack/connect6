import itertools
import datetime
from gameboard import GameBoard 
from coord import Coord
from referee import Referee
from player import Player
from dummyai import DummyAI


class Game:

	
	def run(self):
		ref = Referee()
		p1 = Player()
		p2 = DummyAI()

		ref.add_player(p1)
		ref.add_player(p2)

		

if __name__ == "__main__":
		
	g = Game()
	g.run()

		


		
			
		
		
				
	