from world import World
from file_parser import File_Parser

world = World()
world.generate_world("world_1.txt")

print(world.world)
