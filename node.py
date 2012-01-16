class Node:

	__children = []
	__board = None
	__parent = None


	def __init__(self, board):
		self.__board = board

	def add_child(self,child_node):
		child_node.set_parent(self)
		self.__children.append(child_node)

	def set_parent(self,parent_node):
		self.__parent = parent_node

	def get_children(self):
		return self.__children

	def is_root(self):
		return True if __parent == None else False

	def get_parent(self):
		return __parent