"""
"	Authors: 	Nicolas Neu & Dennis Zimmermann
"	Date:		20. January 2012
"
"	Rule based KI for Connect6
"
"	Open Issues:
"		- Diagonal Rows
"		- Error in referee 
"""

from referee import Referee
from player import Player
from dummyai import DummyAI


class Game:

	
	def run(self):
		ref = Referee()
		p2 = Player()
		p1 = Player()

		ref.add_player(p1)
		ref.add_player(p2)

		

if __name__ == "__main__":
		
	g = Game()
	g.run()

		



				
	