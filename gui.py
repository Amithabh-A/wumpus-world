from tkinter import *
from agent import Agent
from world import World
import time

# creating main tkinter window/toplevel
master = Tk()
master.title("Wumpus World")

# 	bg - The normal background color displayed behind the label and indicator.

"""
l1 = Label(master, text = "A", height = 5, width = 11, relief=RIDGE)
l2 = Label(master, text = "W", height = 5, width = 11, relief=RIDGE)
l3 = Label(master, text = "S", height = 5, width = 11, relief=RIDGE)
l4 = Label(master, text = "P", height = 5, width = 11, relief=RIDGE)
"""


class Grid_Label():
    def __init__(self, i, j):
        self.text = StringVar()
        self.label = Label(master, textvariable = self.text, height = 5, width = 11, relief = RIDGE)
        self.label.grid(row = i, column = j, sticky = W, pady = 1)
        self.row = i
        self.col = j
    def change_text(self, updated_text):
        self.text.set(str(updated_text))

world = World()
world.generate_world("world_1.txt")
label_grid = [[Grid_Label(i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]
agent = Agent(world, label_grid)

def solve_wumpus_world():
    # Agent Solving
    while agent.exited == False:
        agent.explore()
        if agent.found_gold == True:
            agent.leave_cave()
        break
    print("You have exited with the gold!")
    agent.repaint_world()
    agent.world_knowledge[agent.world.agent_row][agent.world.agent_col].remove('A')
    time.sleep(1.5)
    agent.repaint_world()


start = Button(master, text="Start", command=solve_wumpus_world)
start.grid(row = 0, column = len(label_grid[0]), sticky = W, pady = 1)

mainloop()
