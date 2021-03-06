"""
"	Authors: 	Nicolas Neu & Dennis Zimmermann
"	Date:		20. January 2012
"
"	Rule based AI for Connect6
"
"	Open Issues:
"		- Diagonal Rows
"		- Error in referee 
"""

class Coord:
	
	row = None
	col = None

	def __init__(self,row,col):
		if row > 18:
			row = 18
		elif row < 0:
			row = 0

		if col > 18:
			col = 18
		elif col < 0:
			col = 0
		
		self.row = row 
		self.col = col 


	 

	def get_msg_repr(self):
		if self.row >= 10:
			r = str(self.row)
		else:
			r = str(0)+str(self.row)

		if self.col >= 10:
			c = str(self.col)
		else:
			c = str(0)+str(self.col)
		
		return str(r+c)

	def __str__(self):
		return "("+str(self.row)+","+str(self.col)+")"

	def __repr__(self):
		return self.__str__()

	def __eq__(self,coord):
		return self.row == coord.row and self.col == coord.col

	def __hash__(self):
		return int("1"+self.get_msg_repr())
		

		