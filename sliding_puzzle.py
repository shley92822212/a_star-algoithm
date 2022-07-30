#file sliding_puzzle.py
#student Ashley FOley 19178703
class SlidingPuzzle:

    def __init__(self):
        pass

    def heuristic(self, state):
        count = 0
        for i in range(7):
            if state[i] == "B":
                for o in range(7):
                    if state[o] == "W":
                        if o > i:
                            count = count + 1
        return count

    def swap(self, src_index, dst_index, state):
        state[src_index], state[dst_index] = state[dst_index], state[src_index]
        return state


    def gen_children(self, state):
        return_states = []
        if state.index("-") == 0:
            return_states.append(self.swap(0, 1, state.copy()))
            return_states.append(self.swap(0, 2, state.copy()))
            return_states.append(self.swap(0, 3, state.copy()))
        elif state.index("-") == 1:
            return_states.append(self.swap(1, 0, state.copy()))
            return_states.append(self.swap(1, 2, state.copy()))
            return_states.append(self.swap(1, 3, state.copy()))
            return_states.append(self.swap(1, 4, state.copy()))
        elif state.index("-") == 2:
            return_states.append(self.swap(2, 0, state.copy()))
            return_states.append(self.swap(2, 1, state.copy()))
            return_states.append(self.swap(2, 3, state.copy()))
            return_states.append(self.swap(2, 4, state.copy()))
            return_states.append(self.swap(2, 5, state.copy()))
        elif state.index("-") == 3:
            return_states.append(self.swap(3, 0, state.copy()))
            return_states.append(self.swap(3, 1, state.copy()))
            return_states.append(self.swap(3, 2, state.copy()))
            return_states.append(self.swap(3, 4, state.copy()))
            return_states.append(self.swap(3, 5, state.copy()))
            return_states.append(self.swap(3, 6, state.copy()))
        elif state.index("-") == 4:
            return_states.append(self.swap(4, 1, state.copy()))
            return_states.append(self.swap(4, 2, state.copy()))
            return_states.append(self.swap(4, 3, state.copy()))
            return_states.append(self.swap(4, 5, state.copy()))
            return_states.append(self.swap(4, 6, state.copy()))
        elif state.index("-") == 5:
            return_states.append(self.swap(5, 2, state.copy()))
            return_states.append(self.swap(5, 3, state.copy()))
            return_states.append(self.swap(5, 4, state.copy()))
            return_states.append(self.swap(5, 6, state.copy()))
        elif state.index("-") == 6:
            return_states.append(self.swap(6, 3, state.copy()))
            return_states.append(self.swap(6, 4, state.copy()))
            return_states.append(self.swap(6, 5, state.copy()))
        return return_states


    def check_goal(self, state):
        self.heuristic(state)
        if self.heuristic(state) == 0:
            return True
        return False


    def cost(self, parent_cost, state, parent_state):
        jump = state.index("-") - parent_state.index("-")
        if jump < 0:
            jump = jump*-1
        if jump != 1:
            jump = jump - 1
        return parent_cost + jump

    def print_state(self, state):
        print(state)