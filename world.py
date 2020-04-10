from file_parser import File_Parser

class World:
    def __init__(self):
        self.world = [[]]
        # print("World generated")

    def generate_world(self, file_name):

        file_parser = File_Parser(file_name)
        """
        print(file_parser.row_col)
        print(file_parser.agent)
        print(file_parser.wumpus)
        print(file_parser.gold)
        print(file_parser.pits)
        """
        self.world = [[0 for i in range(int(file_parser.row_col[1]))] for j in range(int(file_parser.row_col[0]))]
        self.world[int(file_parser.agent[1])][int(file_parser.agent[2])] = file_parser.agent[0]
        self.world[int(file_parser.wumpus[1])][int(file_parser.wumpus[2])] = file_parser.wumpus[0]
        self.world[int(file_parser.gold[1])][int(file_parser.gold[2])] = file_parser.gold[0]
        for pit in file_parser.pits:
            self.world[int(pit[1])][int(pit[2])] = pit[0]



    def populate_indicators(self):
        ...
        # breezes, stenches
