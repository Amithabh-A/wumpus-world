# Wumpus World Simulation

Wumpus World is the representation of a simple world where an explorer searches a dark,
dangerous cave in search for a bounty of gold. In this cave, there are two threats to the explorer’s life:
falling in bottomless pits (**P**) and being slain by the Wumpus (**W**). The explorer’s goal is to find the gold (**G**) then exit safely by backtracking through the cave. Typically, the cave is represented by a 4×4 grid or 16
rooms. Each room will have indicators that can be detected by the explorer. If the explorer smells a
stench (**S**) that means that Wumpus may be in an adjacent tile. If the explorer feels a breeze (**B**) that means that a bottomless pit may be in an adjacent tile. If the agent sees glitter that means that there is gold in the
current room and upon retrieval of the gold, the explorer is allowed to leave the cave. While exploring
the cave, the explorer gathers knowledge and acts according to the gathered knowledge; this type of
behavior makes the explorer a knowledge-based agent.

### Knowledge Representation
- A = Agent
- G = Gold
- W = Wumpus
- S = Stench
- P = Pit
- B = Breeze

```
4 4
A 3 0
W 1 0
G 1 1
P 0 3
P 1 2
P 3 2
```

![Figure 1](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_1.png?raw=true)
![Figure 2](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_2.png?raw=true)
![Figure 3](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_3.png?raw=true)
![Figure 4](https://github.com/alexander-bachmann/wumpus-world/blob/master/README_images/figure_4.png?raw=true)


- Execution:
```
$ python gui.py
```
- Requires [Python 3.7.x](https://www.python.org/downloads/release/python-376/) or later
