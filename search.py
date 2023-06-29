from file_parser import File_Parser
from world import World
import util


class Search:
    def __init__(self, world_file):
        self.file_parser = File_Parser(world_file)
        self.world = World()
        self.world.generate_world(world_file)
        self.start_state = tuple(self.file_parser.agent)
        self.end_state = tuple(self.file_parser.gold)
        
    

    def get_world(self):
        return self.world.world
    
    def breadth_first_search(self):

        #assuming that gold will not be present in start node

        from util import Queue

        Frontier=Queue()
        #frontier contains the unexplored nodes(RELEVANT) ordered with respect to the estimated minimum cost 
        #of path from startState to Goal state through that node. 

        PathQueue=Queue()
        #PathQueue stores the cost of the paths for each nodes in the Frontier(i.e, the priority queue that
        #contains the unexplored RELEVANT nodes. )

        #GUTENS of this procedure : eventually the Goal State will be added to the Frontier(unexplored
        #RELEVANT priority queue) and when it is popped, we get the exact minimum cost path from the startState
        #to the goalState. The only thing heuristic do is to reduce the search space. 

        exploredStates=[]
        currentPath=[]


        Frontier.push()
        currentState=Frontier.pop()

        while(problem.isGoalState(currentState)==False):
            if currentState not in exploredStates:
                exploredStates.append(currentState)

                Successors =problem.getSuccessors(currentState)
                for Successor in Successors:
                    if Successor not in exploredStates:
                        #cost=problem.getCostOfActions(currentPath+[Successor[1]])
                        #cost+=heuristic(Successor[0],problem)
                        Frontier.push(Successor[0])
                        PathQueue.push(currentPath+[Successor[1]])
                currentPath=PathQueue.pop()
                currentState=Frontier.pop()
            else:
                currentPath=PathQueue.pop()
                currentState=Frontier.pop()

        return currentPath
'''
search = Search('world.txt')
l = search.get_world()
for row in l:
    for col in row:
        print(col,end=" ")
    print()
'''