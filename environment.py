# MazeQLearning/environment.py

from maze import maze
from typing import Tuple

class Environment:

    def __init__(self) -> None:
        pass

    def getNextState(self, state: Tuple[int, int], action: str) -> Tuple[Tuple[int, int], bool]:
        row = state[0]
        column = state[1]
        if action == 'up':
            row -= 1
        elif action == 'down':
            row += 1
        elif action == 'left':
            column -= 1
        elif action == 'right':
            column += 1
        nextState = (row, column)
        try:
            # Beyond the boundary or hit the wall.
            if row < 0 or column < 0 or maze[row, column] == 1:
                return (state, False)
            # Goal
            elif maze[row, column] == 2:
                return (nextState, True)
            # Forward
            else:
                return (nextState, False)
        except IndexError as e:
            # Beyond the boundary.
            return (state, False)

    def doAction(self, state: Tuple[int, int], action: str) -> Tuple[int, Tuple[int, int], bool]:
        nextState, result = self.getNextState(state, action)
        # No move
        if nextState == state:
            reward = -10
        # Goal
        elif result:
            reward = 100
        # Forward
        else:
            reward = -1
        return (reward, nextState, result)
