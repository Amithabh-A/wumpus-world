from tkinter import *
from agent import Agent
from world import World
# from pandas import *
from grid_label import Grid_Label
import time

def solve_wumpus_world(master, world_file):
    world = World()
    world.generate_world(world_file)
    # print(DataFrame(world.world))
    label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]
    agent = Agent(world, label_grid)

    # Agent Solving
    while agent.exited == False:
        agent.explore()
        if agent.found_gold == True:
            agent.leave_cave()
        break
    # print("You have exited with the gold!")
    agent.repaint_world()
    agent.world_knowledge[agent.world.agent_row][agent.world.agent_col].remove('A')
    time.sleep(1.5)
    agent.repaint_world()


master = Tk()
master.title("Wumpus World")

world = World()
world.generate_world("world_1.txt")
label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]
# agent = Agent(world, label_grid)
solve_wumpus_world(master, "world_1.txt")

mainloop()
