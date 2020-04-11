from world import World
from file_parser import File_Parser
from agent import Agent
from pandas import * # pip install pandas  --  will eventually remove

world = World()
world.generate_world("world_1.txt")
agent = Agent(world)

# print(DataFrame(world.world))
print(DataFrame(agent.world_knowledge))

while agent.is_dead() == False:
    direction = input("Move (u, r, d, l): ")
    agent.move(direction)
    # print(DataFrame(world.world))
    print(DataFrame(agent.world_knowledge))
