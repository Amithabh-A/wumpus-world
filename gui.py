from tkinter import *
from human import Agent
from world import World
from keyboard_input import Keyboard_Input
from grid_label import Grid_Label
#import time
global_key_input=None

def solve_wumpus_world(master, world_file):
    
    world = World()
    world.generate_world(world_file)
    # print(DataFrame(world.world))
    label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]
    agent = Agent(world, label_grid)
    
    while agent.exited == False:
        #agent.explore()
        master.bind('<Left>', 
                    lambda event: agent.move('l'))
        master.bind('<Right>', 
                    lambda event: agent.move('r'))
        master.bind('<Up>', 
                    lambda event: agent.move('u'))
        master.bind('<Down>', 
                    lambda event: agent.move('d'))
        
        #master.bind("<KeyPress>", pressed)
        
        agent.move(global_key_input)
        
        agent.repaint_world()

        if agent.valid_exit() == True:
            print("hi")
            break
        else:
            #print('no')
            pass
        # if agent.found_gold == True:
        #     agent.leave_cave()
        #break
        #initial()   
    print("You have exited with the gold!")
    agent.repaint_world()
    try:
        agent.world_knowledge[agent.world.agent_row][agent.world.agent_col].remove('A')
    except ValueError:
        pass
    agent.repaint_world()
    
master = Tk()
master.title("Wumpus World")
key = Keyboard_Input(master)


world = World()
world.generate_world("world.txt")
label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]

solve_wumpus_world(master, "world.txt")
mainloop()
