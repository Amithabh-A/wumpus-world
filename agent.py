class Agent:
    def __init__(self, world):
        self.world = world
        self.world_knowledge = [[[] for i in range(self.world.num_cols)] for j in range(self.world.num_rows)]
        self.world_knowledge[self.world.agent_row][self.world.agent_col].append('A')
        self.mark_tile_visited()

    def move(self, direction):

        successful_move = False
        # each move makes predictions based on indicators of where pits and wumpus are
        if direction == 'u':
            successful_move = self.move_up()
        if direction == 'r':
            successful_move = self.move_right()
        if direction == 'd':
            successful_move = self.move_down()
        if direction == 'l':
            successful_move = self.move_left()

        if successful_move:
            self.add_indicators_to_knowledge()
            self.mark_tile_visited()
            self.predict_wumpus()
            self.predict_pits()

        return successful_move

    def add_indicators_to_knowledge(self):
        if 'B' in self.world.world[self.world.agent_row][self.world.agent_col]:
            if 'B' not in self.world_knowledge[self.world.agent_row][self.world.agent_col]:
                self.world_knowledge[self.world.agent_row][self.world.agent_col].append('B')
        if 'S' in self.world.world[self.world.agent_row][self.world.agent_col]:
            if 'S' not in self.world_knowledge[self.world.agent_row][self.world.agent_col]:
                self.world_knowledge[self.world.agent_row][self.world.agent_col].append('S')
        if 'G' in self.world.world[self.world.agent_row][self.world.agent_col]:
            if 'G' not in self.world_knowledge[self.world.agent_row][self.world.agent_col]:
                self.world_knowledge[self.world.agent_row][self.world.agent_col].append('G')
        if 'P' in self.world.world[self.world.agent_row][self.world.agent_col]:
            if 'P' not in self.world_knowledge[self.world.agent_row][self.world.agent_col]:
                self.world_knowledge[self.world.agent_row][self.world.agent_col].append('P')
        if 'W' in self.world.world[self.world.agent_row][self.world.agent_col]:
            if 'W' not in self.world_knowledge[self.world.agent_row][self.world.agent_col]:
                self.world_knowledge[self.world.agent_row][self.world.agent_col].append('W')

    def predict_pits(self):
        try:
            if 'B' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_row-1 >= 0:
                    if '.' not in self.world.world[self.world.agent_row-1][self.world.agent_col]:
                        if 'p' not in self.world_knowledge[self.world.agent_row-1][self.world.agent_col]:
                            self.world_knowledge[self.world.agent_row-1][self.world.agent_col].append('p')
        except IndexError:
            pass

        try:
            if 'B' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_col+1 < self.world.num_cols:
                    if '.' not in self.world.world[self.world.agent_row][self.world.agent_col+1]:
                        if 'p' not in self.world_knowledge[self.world.agent_row][self.world.agent_col+1]:
                            self.world_knowledge[self.world.agent_row][self.world.agent_col+1].append('p')
        except IndexError:
            pass

        try:
            if 'B' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_row+1 < self.world.num_rows:
                    if '.' not in self.world.world[self.world.agent_row+1][self.world.agent_col]:
                        if 'p' not in self.world_knowledge[self.world.agent_row+1][self.world.agent_col]:
                            self.world_knowledge[self.world.agent_row+1][self.world.agent_col].append('p')
        except IndexError:
            pass

        try:
            if 'B' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_col-1 >= 0:
                    if '.' not in self.world.world[self.world.agent_row][self.world.agent_col-1]:
                        if 'p' not in self.world_knowledge[self.world.agent_row][self.world.agent_col-1]:
                            self.world_knowledge[self.world.agent_row][self.world.agent_col-1].append('p')
        except IndexError:
            pass


    def predict_wumpus(self):
        try:
            if 'S' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_row-1 >= 0:
                    if '.' not in self.world.world[self.world.agent_row-1][self.world.agent_col]:
                        if 'w' not in self.world_knowledge[self.world.agent_row-1][self.world.agent_col]:
                            self.world_knowledge[self.world.agent_row-1][self.world.agent_col].append('w')
        except IndexError:
            pass

        try:
            if 'S' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_col+1 < self.world.num_cols:
                    if '.' not in self.world.world[self.world.agent_row][self.world.agent_col+1]:
                        if 'w' not in self.world_knowledge[self.world.agent_row][self.world.agent_col+1]:
                            self.world_knowledge[self.world.agent_row][self.world.agent_col+1].append('w')
        except IndexError:
            pass

        try:
            if 'S' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_row+1 < self.world.num_rows:
                    if '.' not in self.world.world[self.world.agent_row+1][self.world.agent_col]:
                        if 'w' not in self.world_knowledge[self.world.agent_row+1][self.world.agent_col]:
                            self.world_knowledge[self.world.agent_row+1][self.world.agent_col].append('w')
        except IndexError:
            pass

        try:
            if 'S' in self.world.world[self.world.agent_row][self.world.agent_col]:
                if self.world.agent_col-1 >= 0:
                    if '.' not in self.world.world[self.world.agent_row][self.world.agent_col-1]:
                        if 'w' not in self.world_knowledge[self.world.agent_row][self.world.agent_col-1]:
                            self.world_knowledge[self.world.agent_row][self.world.agent_col-1].append('w')
        except IndexError:
            pass




    def clean_wumpus_predictions(self):
        ...



    def move_up(self):
        try:
            if self.world.agent_row-1 >= 0:
                self.remove_agent()
                self.world.agent_row -= 1
                self.add_agent()
                return True
            else:
                return False
        except IndexError:
            return False


    def move_right(self):
        try:
            if self.world.agent_col+1 < self.world.num_cols:
                self.remove_agent()
                self.world.agent_col += 1
                self.add_agent()
                return True
            else:
                return False
        except IndexError:
            return False


    def move_down(self):
        try:
            if self.world.agent_row+1 < self.world.num_rows:
                self.remove_agent()
                self.world.agent_row += 1
                self.add_agent()
                return True
            else:
                return False
        except IndexError:
            return False


    def move_left(self):
        try:
            if self.world.agent_col-1 >= 0:
                self.remove_agent()
                self.world.agent_col -= 1
                self.add_agent()
                return True
            else:
                return False
        except IndexError:
            return False


    def remove_agent(self):
        self.world.world[self.world.agent_row][self.world.agent_col].remove('A')
        self.world_knowledge[self.world.agent_row][self.world.agent_col].remove('A')


    def add_agent(self):
        self.world.world[self.world.agent_row][self.world.agent_col].append('A')
        self.world_knowledge[self.world.agent_row][self.world.agent_col].append('A')


    def mark_tile_visited(self):
        if '.' not in self.world_knowledge[self.world.agent_row][self.world.agent_col]:
            self.world.world[self.world.agent_row][self.world.agent_col].append('.')
            self.world_knowledge[self.world.agent_row][self.world.agent_col].append('.')


    def is_dead(self):
        if 'W' in self.world.world[self.world.agent_row][self.world.agent_col]:
            print("You have been slain by the Wumpus!")
            return True
        elif 'P' in self.world.world[self.world.agent_row][self.world.agent_col]:
            print("You have fallen in a pit!")
            return True
        else:
            return False
