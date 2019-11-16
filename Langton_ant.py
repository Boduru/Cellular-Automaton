from copy import copy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


def is_alive(pos):
	"""Check if a cell is alive"""

	if is_grid_contain(pos):
		return grid[pos[0]][pos[1]]
	return 0


def get_new_dir(new_dir):
	"""Compute new direction"""

	global direction

	direction += new_dir

	if direction == 4:
		direction = 0
	elif direction == -1:
		direction = 3

	return direction


def turn(ant, new_dir):
	"""Chanage ant's direction """

	if new_dir == BOTTOM:
		ant[1] += 1
	elif new_dir == UP:
		ant[1] -= 1
	elif new_dir == RIGHT:
		ant[0] += 1
	else:
		ant[0] -= 1

	return ant


def is_grid_contain(pos):
	"""Check if grid contains wanted cell"""

	return pos[0] >= 0 and pos[1] >= 0 and \
	pos[0] < len(grid) and pos[1] < len(grid)

  
def get_ant_cell():
	"""Extract ant's cell indexes"""

	res = np.where(grid == 2)
	return [*res[0], *res[1]]


def update(i):
	"""Update grid"""

	global grid, ant

	if is_alive(ant):
		grid[ant[0]][ant[1]] = 0
		new_dir = -1
	else:
		grid[ant[0]][ant[1]] = 1
		new_dir = 1

	direction = get_new_dir(new_dir)
	ant = turn(ant, direction)
	display_grid = grid.copy()
	display_grid[ant[0]][ant[1]] = 2

	return mat.set_array(display_grid)


def create_grid(n, p=0):
	"""Create grid"""

	return np.random.choice([1, 0], n*n, p=[p, 1-p]).reshape(n, n)


def put_ant(grid, ant):
	"""Place ant into the grid"""

	grid[ant[0]][ant[1]] = 2

	return grid


LEFT = 0
UP = 1
RIGHT = 2
BOTTOM = 3
SIZE = 100
grid = create_grid(SIZE)
ant = [int(SIZE / 2), int(SIZE / 2)]
grid = put_ant(grid, ant)
direction = UP

# set up animation
fig, ax = plt.subplots()
cmap = ListedColormap(['white', 'black', 'blue'])
mat = ax.matshow(grid, cmap=cmap)
ax.legend(loc="upper left")
ani = FuncAnimation(fig, update, frames=20000, interval=1)
plt.show()