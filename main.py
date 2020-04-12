from world import World
from agent import Agent

world = World()
world.generate_world("world_1.txt")
agent = Agent(world)

# Agent Solving
while agent.exited == False:
    agent.explore()
    if agent.found_gold == True:
        agent.leave_cave()
    break

print("You have exited with the gold!")
