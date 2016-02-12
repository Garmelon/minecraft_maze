import sys
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

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
	
	DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # directions a player can move in
	SYMBOLS = {" ": "░░", "?": "▒▒", "o": "  ", "x": "██"} # symbols for the different cell types
	COLORS = {" ": [.5, .5, .5], "?": [.5, 0, 0], "x": [0, 0, 0], "o": [1, 1, 1]}
	
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
		
		Convert the maze to string representation.
		This function shows boundary walls around the maze.
		"""
		s = "".join([self.SYMBOLS["x"] for i in range(self.x + 2)]) + "\n"
		for row in self.maze:
			s += "{0}{1}{0}\n".format(self.SYMBOLS["x"], "".join([self.SYMBOLS["o"] if type(cell) is int else self.SYMBOLS[cell] for cell in row]))
		s += "".join([self.SYMBOLS["x"] for i in range(self.x + 2)])
		return s
	
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
	
	def mark_adjacent(self, x, y):
		"""
		-> None
		
		Marks all cells adjacent to x, y as "?" and add them to the queue.
		"""
		for xn, yn in self.get_neighbours(x, y):
			if self.get_cell(xn, yn) == " ":
				self.set_cell(xn, yn, "?")
				self.queue.append((xn, yn))
	
	def replace(self, val1, val2):
		"""
		-> None
		
		Replace all occurrences of val1 with another val2.
		"""
		for x in range(self.x):
			for y in range(self.y):
				if self.get_cell(x, y) == val1:
					self.set_cell(x, y, val2)
	
	def replace_integers(self, val):
		"""
		-> None
		
		Replace all integers with val.
		"""
		for x in range(self.x):
			for y in range(self.y):
				if type(self.get_cell(x, y)) is int:
					self.set_cell(x, y, val)
	
	def get_neighbours(self, x, y):
		"""
		-> list of neighbours
		
		Return a list of coordinate tuples of neighbours of the cell at x, y.
		"""
		neighbours = []
		for xd, yd in self.DIRECTIONS:
			xd, yd = xd + x, yd + y
			if self.in_boundaries(xd, yd):
				neighbours.append((xd, yd))
		return neighbours
	
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
		Also resets the queue, seed points and gif frame name count.
		"""
		self.queue = []
		self.points = []
		self.count = 0 # gif frame file names
		self.maze = [[" " for y in range(self.x)] for x in range(self.y)]
	
	def fill(self, points=None):
		"""
		-> None
		
		Add the start and the end point and a few random seeds to the maze.
		To manually add seed points (for example starting or end points)
		in addition to the randomly generated seed points, specify their
		coordinates as tuples in the points list:
		fill([(x1, y1), (x2, y2)])
		"""
		if points is None:
			points = []
		for i in range((self.x//10)*(self.y//10)): # add random points
			points.append((random.randrange(self.x), random.randrange(self.y)))
		for i in range(len(points)): # add points to map
			x, y = points[i]
			self.set_cell(x, y, i)
			for xn, yn in self.get_neighbours(x, y):
				cell = self.get_cell(xn, yn)
				if type(cell) is int and not cell == i:
					self.replace(cell, i)
		for x, y in points:
			self.mark_adjacent(x, y)
		self.points = points
	
	def generate(self, x_start, y_start, x_end, y_end, gif_path=None):
		"""
		-> None
		
		Generate a new maze layout.
		x_start, y_start: coordinates of the starting point
		x_end, y_end    : coordinates of the end point
		
		If you want to generate a gif detailing the generation process:
		Specify a path to an empty folder as gif_path. Every step in
		the generation process, a frame displaying the current state
		will be saved in the folder (maze_xxxxxxxx.png). You will have
		to combine the frames into a gif yourself.
		"""
		# initializing the maze
		self.reset()
		if gif_path:
			for i in range(10):
				self.save_gif_frame(gif_path)
		self.fill([(x_start, y_start), (x_end, y_end)])
		if gif_path:
			for i in range(10):
				self.save_gif_frame(gif_path)
		
		# actual maze making algorithm
		while self.queue:
			x_cur, y_cur = self.queue_pop_random()
			# find all neighbours which are a path (coordinates)
			neighbours = [(xn, yn) for xn, yn in self.get_neighbours(x_cur, y_cur) if type(self.get_cell(xn, yn)) is int]
			# find all unique neighbour webs (connected paths) (id of the web)
			neighbour_webs = []
			for xn, yn in neighbours:
				cell = self.get_cell(xn, yn)
				if not cell in neighbour_webs:
					neighbour_webs.append(cell)
			# determine the current cell's "state"
			if len(neighbour_webs) == 1:
				if len(neighbours) > 1:
					self.set_cell(x_cur, y_cur, "x")
				else:
					self.set_cell(x_cur, y_cur, neighbour_webs[0])
					self.mark_adjacent(x_cur, y_cur)
			else:
				self.set_cell(x_cur, y_cur, neighbour_webs[0])
				self.mark_adjacent(x_cur, y_cur)
				for web in neighbour_webs[1:]:
					self.replace(web, neighbour_webs[0])
			# draw the gif frame
			if gif_path:
				self.save_gif_frame(gif_path)
		
		# finishing touches
		self.replace(" ", "x")
		self.replace_integers("o")
		if gif_path:
			for i in range(20):
				self.save_gif_frame(gif_path)
	
	def save_image(self, path):
		"""
		-> None
		
		Save a png image of the maze in path.
		"""
		cells = []
		cells.append([self.COLORS["x"] for i in range(self.x + 2)])
		for row in self.maze:
			cells.append([self.COLORS["x"]] + [col.hsv_to_rgb([cell/len(self.points), .5, 1]) if type(cell) is int else self.COLORS[cell] for cell in row] + [self.COLORS["x"]])
		cells.append([self.COLORS["x"] for i in range(self.x + 2)])
		cells = np.array(cells)
		plt.imsave(path, cells)
	
	def save_gif_frame(self, path):
		self.save_image("{}maze_{:0>8}.png".format(path, self.count))
		self.count += 1
	
	def get_stats(self):
		"""
		-> amount of paths, amount of walls
		
		Count and return the amount of paths and walls in the maze.
		NOTE: The outside walls aren't a part of the maze.
		"""
		paths = 0
		walls = 0
		for x in range(self.x):
			for y in range(self.y):
				cell = self.get_cell(x, y)
				if type(cell) is int or cell == "o":
					paths += 1
				elif cell == "x":
					walls += 1
		return paths, walls

def main(args):
	if args[1] in ["-h", "--help"]:
		print("Script to create mazes! Yay!\n")
		print("Usage:")
		print("    python3 maze.py x_size y_size x_start y_start x_end y_end[ image_path[ gif_path]]\n")
		print("    x_size, y_size  : size of the maze")
		print("    x_start, y_start: coordinates of starting point")
		print("    x_end, y_end    : coordinates of end point")
		print("    image_path      : image location")
		print("    gif_path        : path to folder to store gif frames in")
		return
	
	maze = Maze(*[int(arg) for arg in args[1:3]])
	if len(args) >= 9:
		print("Saving gif frames to {}".format(args[8]))
		maze.generate(*[int(arg) for arg in args[3:7]], gif_path=args[8])
	else:
		maze.generate(*[int(arg) for arg in args[3:7]])
	print(maze)
	paths, walls = maze.get_stats()
	print("Paths: {}\nWalls: {}".format(paths, walls))
	if len(args) >= 8:
		maze.save_image(args[7])
		print("Saved maze to {}".format(args[7]))
	
if __name__ == "__main__":
	main(sys.argv)
