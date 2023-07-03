from tkinter import *
from human import Agent
from world import World
from keyboard_input import Keyboard_Input
from grid_label import Grid_Label
from sample import *
import curses
#import time

def solve_wumpus_world(master, world_file):
    
    world = World()
    world.generate_world(world_file)
    # print(DataFrame(world.world))
    label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]
    agent = Agent(world, label_grid)
    
    while agent.exited == False:
        #agent.explore()

        #user pressing the arrow key
        key = curses.wrapper(capture_key)
        #print(key.get_key())
        agent.move(key)



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
    
    print("You have exited with the gold!")
    agent.repaint_world()
    try:
        agent.world_knowledge[agent.world.agent_row][agent.world.agent_col].remove('A')
    except ValueError:
        pass
    agent.repaint_world()

def capture_key(stdscr):
    curses.halfdelay(1)  # Set a timeout for non-blocking input
    key = stdscr.getch()

    if key == curses.KEY_UP:
        return "u"
    elif key == curses.KEY_DOWN:
        return "d"
    elif key == curses.KEY_LEFT:
        return "l"
    elif key == curses.KEY_RIGHT:
        return "r"
    elif key == ord('q'):
        return "q"
    else:
        return None

master = Tk()
master.title("Wumpus World")



world = World()
world.generate_world("world.txt")
label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]

solve_wumpus_world(master, "world.txt")
mainloop()