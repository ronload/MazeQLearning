# MazeQLearning/main.py

import numpy as np
import time
from maze import maze
from maze_window import MazeWindow
from agent import Agent
from environment import Environment
from tqdm import tqdm

def main() -> None:
    initState: tuple = (np.where(maze == -1)[0][0], np.where(maze == -1)[1][0])
    agent: Agent = Agent(maze, initState)
    environment: Environment = Environment()
    with tqdm(total=50, desc='Epoch') as pbar:
        for j in range(50):
            pbar.update(1)
            agent.state = initState
            m.target(agent.state)
            time.sleep(0.1)
            i = 0
            while True:
                i += 1
                action: str = agent.getAction(0.9)
                reward, nextState, result = environment.doAction(agent.state, action)
                agent.updateQTable(action, nextState, reward)
                agent.state = nextState
                m.target(agent.state)
                if result:
                    tqdm.write(f' Iteration {j:2d} : {i} steps to the goal.')
                    break
    agent.showQTable()
m: MazeWindow = MazeWindow(maze)
m.mainloop(main)
