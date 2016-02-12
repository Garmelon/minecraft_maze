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
	NOTE: To access the maze cells: self.maze[y][x] - y first!
	
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
		NOTE: This function doesn't generate a maze layout.
		"""
		self.x = x_size
		self.y = y_size
		self.reset()
	
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
		return x >= 0 and y >= 0 and x < self.x and y < self.y
	
	def get_cell(self, x, y):
		"""
		-> value of the cell
		
		Return the value of the cell at x, y.
		"""
		return self.maze[y][x]
	
	def set_cell(self, x, y, val):
		"""
		-> None
		
		Set the value of the cell at x, y to val.
		"""
		self.maze[y][x] = val
	
	def replace(self, val1, val2):
		"""
		-> None
		
		Replace all occurrences of val1 with another val2.
		"""
		for y in range(self.y):
			for x in range(self.x):
				if self.maze[y][x] == val1:
					self.maze[y][x] = val2
	
	def replace_integers(self, val):
		"""
		-> None
		
		Replace all integers with val.
		"""
		pass
	
	def get_neighbours(self, x, y):
		"""
		-> list of neighbours
		
		Return a list of coordinate tuples of neighbours of the cell at x, y.
		"""
		pass
	
	def queue_pop_random(self):
		"""
		-> coordinate tuple
		
		Pop and return a random coordinate tuple from the queue.
		This function will return None if the queue is empty.
		"""
		if self.queue:
			return self.queue.pop(random.randrange(len(self.queue)))
	
	def reset(self):
		"""
		-> None
		
		Reset the maze to an empty state.
		Also resets the queue, seed points and gif image name count.
		"""
		self.queue = []
		self.points = []
		self.count = 0 # gif image file names
		self.maze = [[" " for y in range(self.x)] for x in range(self.y)]
	
	def fill(self):
		"""
		-> None
		
		Add the start and the end point and a few random seeds to the maze.
		"""
		pass
	
	def generate(self, x_start, y_start, x_end, y_end, gif_path=None):
		"""
		-> None
		
		Generate a new maze layout.
		x_start, y_start: coordinates of the starting point
		x_end, y_end    : coordinates of the end point
		
		If you want to generate a gif detailing the generation process:
		Specify a path to an empty folder as gif_path. Every step in
		the generation process, an image displaying the current state
		will be saved in the folder. You will have to combine these images
		into a gif yourself afterwards.
		"""
		pass
	
	def save_image(self, path):
		"""
		-> None
		
		Save a png image of the maze in path.
		"""
		pass

if __name__ == "__main__":
	maze = Maze(*sys.argv[1:])
	maze.generate()
	print(maze)
	stats = maze.get_stats()
	print("Paths: {}\nWalls: {}".format(stats["o"], stats["x"]))
	maze.save_image("maze.png")
	print("Saved maze as maze.png")