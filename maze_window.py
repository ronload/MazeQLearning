# MazeQLearning/maze_window.py

import numpy as np
import tkinter as tk
from typing import List, Tuple

class MazeWindow:

    def __init__(self, maze: np.array) -> None:
        self.root = tk.Tk()
        self.root.title('Maze Q-learning')
        self.maze = maze
        self.labels: List[List[tk.Label]] = np.zeros(self.maze.shape, dtype=object).tolist()
        self.plotBackground()

    def plotBackground(self) -> None:
        for i, row in enumerate(self.maze.tolist()):
            for j, element in enumerate(row):
                bg = 'black' if element == 1 else 'red' if element == 2 else 'green' if element == -1 else 'white'
                self.labels[i][j] = tk.Label(self.root, foreground='blue', background=bg, width=2, height=1, relief='ridge', font='? 40 bold')
                self.labels[i][j].grid(row=i, column=j)

    def mainloop(self, func) -> None:
        self.root.after(1000, func)
        self.root.mainloop()
        
    def target(self, indexes: Tuple[int, int]) -> None:
        for label in [item for row in self.labels for item in row]:
            label.config(text='')
        self.labels[indexes[0]][indexes[1]].config(text='o')
        self.root.update()
