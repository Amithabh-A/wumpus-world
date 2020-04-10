from file_parser import File_Parser

class World:
    def __init__(self):
        self.world = [[]]
        self.num_rows = 0
        self.num_cols = 0
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
        self.num_rows = int(file_parser.row_col[0])
        self.num_cols = int(file_parser.row_col[1])

        self.world = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.world[int(file_parser.agent[1])][int(file_parser.agent[2])] = file_parser.agent[0]
        self.world[int(file_parser.wumpus[1])][int(file_parser.wumpus[2])] = file_parser.wumpus[0]
        self.world[int(file_parser.gold[1])][int(file_parser.gold[2])] = file_parser.gold[0]
        for pit in file_parser.pits:
            self.world[int(pit[1])][int(pit[2])] = pit[0]


    def populate_indicators(self):
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):

                if self.world[i][j] == 'A':
                    print("Agent at [" + str(i) + ", " + str(j) + "]")

                if self.world[i][j] == 'W':
                    print("Wumpus at [" + str(i) + ", " + str(j) + "]")

                if self.world[i][j] == 'G':
                    print("Gold at [" + str(i) + ", " + str(j) + "]")

                if self.world[i][j] == 'P':
                    print("Pit at [" + str(i) + ", " + str(j) + "]")




        # breezes, stenches
