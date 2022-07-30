#file eight_tile_puzzle.py
#student Ashley FOley 19178703
class TilePuzzle:
    def __init__ (self, goal_state = [1,2,3,4,0,5,6,7,8]):
        self.goal_state = goal_state

    def swap(self, src_index, dst_index, state):
        state[src_index], state[dst_index] = state[dst_index], state[src_index]
        return state

    #Reutrn an list containing each posible state from a given state
    def gen_children(self, state):
        x = state.index(0)%3
        y = state.index(0)//3
        stateList = []
        if x+1 <= 2:
            stateList.append(self.swap(state.index(0), x+1 + 3*y, state.copy()))
        if x-1 >= 0:
            stateList.append(self.swap(state.index(0), x-1 + 3 * y, state.copy()))
        if y + 1 <= 2:
            stateList.append(self.swap(state.index(0), x + 3 * (y + 1), state.copy()))
        if y - 1 >= 0:
            stateList.append(self.swap(state.index(0), x + 3 * (y - 1), state.copy()))
        return stateList


    def check_goal(self, state):
        if state == self.goal_state:
            return True
        return False

    #Returns the heuristic for a given state
    def heuristic(self, state):
        cost = 0
        for value in state:
            v = self.goal_state.index(value)
            gx = v % 3
            gy = v//3
            index = state.index(value)
            x = index%3
            y = index//3
            cost = cost + abs(x - gx) + abs(y - gy)

        return cost
    def cost(self, parent_cost, state, parent_state):
        return parent_cost + 1

    def make_move(self, direction):
        if direction.lower() == "down":
            if self.current_state.index(0) > 5:
                return False
            else:
                self.swap(self.current_state.index(0), self.current_state.index(0) +3, self.current_state)
                return True
        elif direction.lower() == "up":
            if self.current_state.index(0) < 3:
                return False
            else:
                self.swap(self.current_state.index(0), self.current_state.index(0) -3, self.current_state)
                return True
        elif direction.lower() == "left":
            if self.current_state.index(0)%3 == 0:
                return False
            else:
                self.swap(self.current_state.index(0), self.current_state.index(0) - 1, self.current_state)
                return True
        else:
            if self.current_state.index(0) % 3 == 2:
                return False
            else:
                self.swap(self.current_state.index(0), self.current_state.index(0) + 1, self.current_state)
                return True


    def print_state(self, state):
        print(state[0], ", ", state[1], ", ", state[2])
        print(state[3], ", ", state[4], ", ", state[5])
        print(state[6], ", ", state[7], ", ", state[8])