from world import World
from file_parser import File_Parser
from agent import Agent
from pandas import * # pip install pandas  --  will eventually remove

"""
Legend:
. = visited tile
A = agent
G = gold
W = wumpus
S = stench
w = potential wumpus
nw = no wumpus
P = pit
B = breeze
p = potential pit
np = no pit
"""

world = World()
world.generate_world("world_1.txt")
agent = Agent(world)

# print(DataFrame(world.world))
print(DataFrame(agent.world_knowledge))
print("Agent: [" + str(agent.world.agent_row) + ", " + str(agent.world.agent_col) + "]")

# Agent Solving
while agent.exited == False:
    agent.explore()
    if agent.found_gold == True:
        agent.leave_cave()
    break

print("You have exited with the gold!")


"""
# Human Solving
while agent.is_dead() == False:
    direction = input("Move (u, r, d, l): ")
    agent.move(direction)
    # print(DataFrame(world.world))
    print(DataFrame(agent.world_knowledge))
    # print("Number of stenches found: " + str(agent.num_stenches))
"""
