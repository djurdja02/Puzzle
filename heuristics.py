import math


class Heuristic:
    def get_evaluation(self,state):
        pass
class ExampleHeuristic(Heuristic):
    def get_evaluation(self, state):
        return 0

class HammingHeuristic(Heuristic):
    def get_evaluation(self, state):
        n = 0
        for i in range(len(state)):
            if state[i] != 0 and state[i] != i+1:
                n += 1
        return n


class ManhattanHeuristic(Heuristic):
    def get_evaluation(self, state):
        n = 0
        state_len = len(state)
        for i in range(state_len):
            if state[i] == 0:
                continue
            size = math.sqrt(state_len)
            i1 = i // size
            i2 = (state[i]-1) // size
            j1 = i % size
            j2 = (state[i]-1) % size
            n += abs(i1 - i2) + abs(j1 - j2)
        return n
