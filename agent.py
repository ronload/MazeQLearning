# MazeQLearning/agent.py

import numpy as np
import random
from typing import List, Dict, Tuple

class Agent:

    def __init__(self, maze: np.array, initState: Tuple[int, int]) -> None:
        self.state: Tuple[int, int] = initState
        self.maze: np.array = maze
        self.initQTable()
        self.actionList: List[str] = ['up', 'down', 'left', 'right']
        self.actionDict: Dict[str, int] = {element: index for index, element in enumerate(self.actionList)}
    
    def initQTable(self) -> None:
        Q: List[List[List[float]]] = np.zeros(self.maze.shape).tolist()
        for i, row in enumerate(Q):
            for j, _ in enumerate(row):
                Q[i][j] = [0, 0, 0, 0]  # up, down, left, right
        self.QTable: np.array = np.array(Q, dtype='f')
    
    def showQTable(self) -> None:
        for i, row in enumerate(self.QTable):
            for j, element in enumerate(row):
                print(f'({i}, {j}){element}')
    
    def showBestAction(self) -> None:
        for i, row in enumerate(self.QTable):
            for j, element in enumerate(row):
                Qa: List[float] = element.tolist()
                action: str = self.actionList[Qa.index(max(Qa))] if max(Qa) != 0 else '??'
                print(f'({i}, {j}){action}', end=" ")
            print()
    
    def getAction(self, eGreddy: float = 0.8) -> str:
        if random.random() > eGreddy:
            return random.choice(self.actionList)
        else:
            Qsa: List[float] = self.QTable[self.state].tolist()
            return self.actionList[Qsa.index(max(Qsa))]
    
    def getNextMaxQ(self, state: Tuple[int, int]) -> float:
        return max(np.array(self.QTable[state]))
    
    def updateQTable(self, action: str, nextState: Tuple[int, int], reward: float, lr: float = 0.7, gamma: float = 0.9) -> None:
        Qs: np.array = self.QTable[self.state]
        Qsa: float = Qs[self.actionDict[action]]
        Qs[self.actionDict[action]] = (1 - lr) * Qsa + lr * (reward + gamma * (self.getNextMaxQ(nextState)))