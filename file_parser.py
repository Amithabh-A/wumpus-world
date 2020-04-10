"""
4 5     # number of rows and cols
A 4 0   # agent starting coordinates
W 1 0   # wumpus coordinates
G 1 1   # gold coordinates
P 0 3   # 1st pit coordinates
P 1 2   # 2nd pit coordinates
P 3 2   # 3rd pit coordinates
"""

class File_Parser:
    def __init__(self, world_file):
        self.world = [[]]

        file = open(world_file, 'r')

        # print(file.splitlines())

        row_col = file.readline()
        row_col = row_col.rstrip('\r\n')
        row_col = row_col.split(" ")
        print(row_col)

        agent = file.readline()
        agent = agent.rstrip('\r\n')
        agent = agent.split(" ")
        print(agent)

        wumpus = file.readline()
        wumpus = wumpus.rstrip('\r\n')
        wumpus = wumpus.split(" ")
        print(wumpus)

        gold = file.readline()
        gold = gold.rstrip('\r\n')
        gold = gold.split(" ")
        print(gold)

        pits = []

        while True:
            pit = file.readline()
            if len(pit) == 0:
                break
            pit = pit.rstrip('\r\n')
            pit = pit.split(" ")

            pits.append(pit)
        print(pits)






        #[[0 for i in range(7)] for j in range(6)]
