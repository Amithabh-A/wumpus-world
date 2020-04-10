from world import World
from file_parser import File_Parser
from pandas import * # pip install pandas  --  will eventually remove

world = World()
world.generate_world("world_1.txt")

print(DataFrame(world.world))
