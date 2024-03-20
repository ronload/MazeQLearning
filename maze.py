# # MazeQLearning/maze.py

import numpy as np

# -1 is origin, 0 is road, 1 is wall, 2 is goal 
maze: np.array = np.array([
    [0, 0, -1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 2]
])