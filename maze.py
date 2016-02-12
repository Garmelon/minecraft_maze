import sys
import random

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.colors as col

class Maze:
	"""
	Maze(x_size, y_size) -> maze
		
	x_size, y_size: The size of the maze in the x and y direction (in cells)
	NOTE: NOT the coordinates of the edge of the maze
	NOTE: The outside walls of the maze aren't a part of the maze
	NOTE: Cell coordinates start at (0|0), not (1|1)
	
	Usage:
	Once you have created an instance, use the generate() function to
	create a maze layout.
	>>> mymaze =  Maze(10, 10, 0, 0, 9, 9)
	>>> mymaze.generate()
	>>> print(mymaze)
	"""
	
	def __init__(self, x_size, y_size):
		"""
		-> None
		
		Initialize the maze. See class docstring for further details.
		"""
		pass
	
	def __str__(self):
		"""
		-> str
		
		Convert the maze to string representation
		"""
		pass
	
	def in_boundaries(self, x, y):
		"""
		-> bool
		
		Return whether the coordinates lie within the boundaries of the maze.
		"""
		pass
	
	def get_cell(self, x, y):
		"""
		-> value of the cell
		
		Return the value of the cell at x, y.
		"""
		pass
	
	def set_cell(self, x, y, val):
		"""
		-> None
		
		Set the value of the cell at x, y to val.
		"""
		pass
	
	def replace(self, val1, val2):
		"""
		-> None
		
		Replace all occurrences of val1 with another val2.
		"""
		pass
	
	def replace_integers(self, val):
		"""
		-> None
		
		Replace all integers with val.
		"""
		pass
	
	def get_neighbours(self, x, y):
		"""
		-> list of neighbours
		
		Return a list of neighbour coordinates of the cell at x, y.
		"""
		pass
	
	def reset(self):
		"""
		-> None
		
		Reset the maze to an empty state. Also resets the queue.
		"""
		pass
	
	def fill(self, x_start, y_start, x_end, y_end, amount):
		"""
		-> None
		
		Add the start and the end point and a few random seeds to the maze.
		"""
		pass
	
	def generate(x_start, y_start, x_end, y_end):
		"""
		-> None
		
		TODO
		"""
		pass