#file a_star.py
#student Ashley FOley 19178703

from eight_tile_puzzle import TilePuzzle
from sliding_puzzle import SlidingPuzzle
class GameState:
    parent = None
    game_type = None
    state = None
    h = None
    depth = 0

    def __init__(self, game_type, state, parent=None):
        self.parent = parent
        self.state = state


        self.game_type = game_type
        if parent != None:
            self.depth = self.game_type.cost(self.parent.depth, self.state, self.parent.state)
        self.h = self.game_type.heuristic(self.state)

    def get_c(self):
        return self.depth

    def get_h(self):
        return self.h

    def get_f(self):
        return self.h + self.depth

    def check_goal(self):
        return self.game_type.check_goal(self.state)

    def get_children(self):
        return self.game_type.gen_children(self.state)

    def print_state(self):
        print(self.get_c(), " depth -- ", self.get_f(), " f")
        self.game_type.print_state(self.state)


class AStar:
    @staticmethod
    def astar():
        game_type = None
        state = ["_", "?", "?", "?", "?", "?", "?", "?", "?"]
        goal = ["_", "?", "?", "?", "?", "?", "?", "?", "?"]
        game = input("8 tile puzzle or sliding tile puzzle (8/s)")
        if game == "8":
            print("Input initial state: ")
            for i in range(9):
                print(state[0], ", ", state[1], ", ", state[2])
                print(state[3], ", ", state[4], ", ", state[5])
                print(state[6], ", ", state[7], ", ", state[8])
                state[i] = int(input("Tile: "))
                if i != 8:
                    state[i+1] = "_"


            print("Input goal state: ")
            for i in range(9):
                print(goal[0], ", ", goal[1], ", ", goal[2])
                print(goal[3], ", ", goal[4], ", ", goal[5])
                print(goal[6], ", ", goal[7], ", ", goal[8])
                goal[i] = int(input("Tile: "))
                if i != 8:
                    goal[i + 1] = "_"

            game_type = TilePuzzle(goal)

        else:
            game_type = SlidingPuzzle()
            print("Input initial state 3 B, 3 W, and 1 -")
            state = ["_", "?", "?", "?", "?", "?", "?"]
            for i in range(7):
                print(state)
                state[i] = input("Tile: ")

        start_node = GameState(game_type, state)

        open_list = []
        closed_list = []

        open_list.append(start_node)

        while len(open_list) > 0:
            open_list.sort(key=lambda x: x.get_f())
            current_node = open_list[0]
            #current_node.print_state()
            #pop the current node and add it to clsoed_lsit
            open_list.pop(0)
            closed_list.append(current_node)

            if current_node.check_goal():
                print("Printing path")
                path = []
                current = current_node
                while current is not None:
                    path.append(current)
                    current = current.parent
                path.reverse()
                for node in path:
                    node.print_state()
                break

            children = current_node.get_children()
            for child in children:
                flag = True
                node = GameState(game_type, child, current_node)
                for check in closed_list:
                    if node.state == check.state:
                        flag = False

                for check2 in open_list:
                    if node.state == check2.state and node.get_c() > check2.get_c():
                        flag = False
                if flag:
                    open_list.append(node)

AStar.astar()

input("Enter to exit")