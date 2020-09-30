# Wumpus World Simulation

## About:

Wumpus World is the representation of a simple world where an explorer searches a dark,
dangerous cave in search for a bounty of gold. In this cave, there are two threats to the explorer’s life:
falling in bottomless pits (**P**) and being slain by the Wumpus (**W**). The explorer’s goal is to find the gold (**G**) then exit safely by backtracking through the cave. Typically, the cave is represented by a 4×4 grid or 16
rooms. Each room will have indicators that can be detected by the explorer. If the explorer smells a
stench (**S**) that means that Wumpus may be in an adjacent tile. If the explorer feels a breeze (**B**) that means that a bottomless pit may be in an adjacent tile. If the agent sees glitter that means that there is gold in the
current room and upon retrieval of the gold, the explorer is allowed to leave the cave. While exploring
the cave, the explorer gathers knowledge and acts according to the gathered knowledge; this type of
behavior makes the explorer a knowledge-based agent.

## Knowledge Representation:
- A = Agent
- G = Gold
- W = Wumpus
- S = Stench
- P = Pit
- B = Breeze

## World Navigation Example:

The following figures will be used to explain the agent’s ability to gather knowledge from its
sensors, store that knowledge, then make predictions about the locations of threats throughout the cave.

![Figure 1](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_1.png?raw=true)
#### Figure 1
The agent, represented by ‘A’, enters the cave from the bottom left [3, 0]. Upon entering the cave, the agent does not perceive any threat indicators.

![Figure 2](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_2.png?raw=true)
#### Figure 2
The agent smelled a stench [2, 0], represented by ‘S’, indicating that the Wumpus must be in an adjacent tile [1, 0] & [2, 1]. From this indicator, the agent predicts all potential locations of the Wumpus and stores that information in its knowledge base.

![Figure 3](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_3.png?raw=true)
#### Figure 3
The agent was forced to backtrack [3, 0] because there was no perceptibly safe move given its current knowledge base.

![Figure 4](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_4.png?raw=true)
#### Figure 4
The agent traveled one tile to the right [3, 1]. In this tile, the agent sensed a breeze indicating that a pit could only be in [3, 2] because a breeze was not sensed when the agent visited [2, 0] in Fig. 2. The agent also further updated its knowledge of the cave by removing its prediction of there being a Wumpus in [2, 1]; the agent was able to remove this prediction because it did not smell a stench in its newly visited tile (all indicators must be adjacent to the possible threat).


## Extension:

Each of the 4 worlds are generated using input .txt files. Modifying the simulation is as easy as customizing one of the four world_*.txt files.

```
4 4
A 3 0
W 1 0
G 1 1
P 0 3
P 1 2
P 3 2
```
*world_1.txt*


- Execution:
```
$ python gui.py
```
- Requires [Python 3.7.x](https://www.python.org/downloads/release/python-376/) or later
