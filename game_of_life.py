import copy
import numpy as np 
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from itertools import product


def get_offsets():
	"""get all eight neighnours"""

	return list(product(*[[0, 1, -1]], repeat=2))[1:]


def get_neighbours(ind):
	"""Calculate neighbours's placements"""

	return np.array([np.array(off) + np.array(ind) for off in OFFSETS])


def is_alive(pos):
	"""Check if cell is alive"""

	if is_grid_contain(pos):
		return grid[pos[0]][pos[1]]
	return 0


def count_neighbours_alive(ind):
	"""Count number of alive neighbours"""

	return sum([1 if is_alive(cell) else 0 for cell in get_neighbours(ind)])


def is_grid_contain(pos):
	"""Check if cell exists"""

	return pos[0] >= 0 and pos[1] >= 0 and \
	pos[0] < len(grid) and pos[1] < len(grid)

    
def update(i):
	"""Update grid"""

	global grid

	new_grid = grid.copy()

	for x in range(len(grid)):
		for y in range(len(grid)):
			nb_neighbours = count_neighbours_alive((x, y))

			if nb_neighbours > 3:
				new_grid[x][y] = 0

			if nb_neighbours == 3:
				new_grid[x][y] = 1

			if nb_neighbours < 2:
				new_grid[x][y] = 0

	grid = new_grid.copy()

	return mat.set_array(new_grid)


def create_grid(n, p=0.5):
	"""Create grid"""

	return np.random.choice([1, 0], n*n, p=[p, 1-p]).reshape(n, n)
	

SIZE = 50
OFFSETS = get_offsets()
grid = create_grid(SIZE)

# set up animation
fig, ax = plt.subplots()
cmap = ListedColormap(['w', 'k'])
mat = ax.matshow(grid, cmap=cmap)
ani = FuncAnimation(fig, update, frames=1000, interval=100)
plt.show()