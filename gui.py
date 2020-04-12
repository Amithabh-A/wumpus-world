from tkinter import *
from agent import Agent
from world import World

# creating main tkinter window/toplevel
master = Tk()

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

"""
for i in range(world.num_rows):
    for j in range(world.num_cols):
        label_grid[i][j].change_text(agent.world_knowledge[i][j])
"""
# Agent Solving
while agent.exited == False:
    agent.explore()
    if agent.found_gold == True:
        agent.leave_cave()
    break

print("You have exited with the gold!")


# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
