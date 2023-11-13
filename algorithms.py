import math
import random
import time

import config


class Algorithm:
    def __init__(self,heuristic=None):
        self.heuristic = heuristic
        self.nodes_evaluated = 0
        self.nodes_generated = 0

    def get_legal_actions(self,state):
        self.nodes_evaluated += 1
        max_index = len(state)
        zero_tile_ind = state.index(0)
        legal_actions = []
        if 0 <= (up_ind := (zero_tile_ind-config.N)) < max_index:
            legal_actions.append(up_ind)
        if 0 <= (right_ind := (zero_tile_ind+1)) < max_index and right_ind % config.N:
            legal_actions.append(right_ind)
        if 0 <= (down_ind := (zero_tile_ind+config.N)) < max_index:
            legal_actions.append(down_ind)
        if 0 <= (left_ind := (zero_tile_ind-1)) < max_index and (left_ind+1) % config.N:
            legal_actions.append(left_ind)
        return legal_actions

    def apply_action(self,state,action):
        self.nodes_generated += 1
        copy_state = list(state)
        zero_tile_ind = state.index(0)
        copy_state[action],copy_state[zero_tile_ind] = copy_state[zero_tile_ind],copy_state[action]
        return tuple(copy_state)

    def get_steps(self,initial_state,goal_state):
        pass

    def get_solution_steps(self,initial_state,goal_state):
        begin_time = time.time()
        solution_actions = self.get_steps(initial_state,goal_state)
        print(f'Execution time in seconds: {(time.time()-begin_time):.2f} | '
              f'Nodes generated: {self.nodes_generated} | '
              f'Nodes evaluated: {self.nodes_evaluated}')
        return solution_actions

class ExampleAlgorithm(Algorithm):
    def get_steps(self, initial_state, goal_state):
        state = initial_state
        solution_actions = []
        while state != goal_state:
            legal_actions = self.get_legal_actions(state)
            action = legal_actions[random.randint(0, len(legal_actions) - 1)]
            solution_actions.append(action)
            state = self.apply_action(state, action)
        return solution_actions


class BestFirstAlgorithm(Algorithm):
    def id(self, state):
        return tuple(state)

    def get_steps(self, initial_state, goal_state):
        state = initial_state
        next_states = []
        solution_actions = []
        actions = dict()
        actions[state] = solution_actions
        while state != goal_state:
            legal_actions = self.get_legal_actions(state)
            for action in legal_actions:
                tmp = self.apply_action(state, action)
                if tmp not in actions:
                    actions[tmp] = solution_actions.copy() + [action]
                    next_states.append((tmp, self.heuristic.get_evaluation(tmp)))
            next_states = sorted(next_states, key=lambda s: (s[1], self.id(s[0])))
            state = next_states.pop(0)[0]
            solution_actions = actions[state].copy()
        return solution_actions


class AStarAlgorithm(Algorithm):
    def ident(self, state):
        return tuple(state)

    def cost(self,path):
        return self.heuristic.get_evaluation(path[-1])+len(path)

    def get_steps(self,initial_state,goal_state):
        state = initial_state
        state_path = [state]
        solution_actions = []
        next_paths = []
        actions = dict()
        while state != goal_state:
            legal_actions = self.get_legal_actions(state)
            for action in legal_actions:
                tmp = self.apply_action(state, action)
                tmp_path = state_path.copy()
                tmp_path.append(tmp)
                if tmp not in actions:
                    actions[tmp] = solution_actions.copy()+[action]
                    next_paths.append((tmp_path, self.cost(tmp_path), self.ident(tmp)))
            next_paths = sorted(next_paths, key=lambda s: (s[1], s[2]))
            state_path = next_paths.pop(0)[0]
            state = state_path[-1]
            solution_actions = actions[state]
        return solution_actions


class BreadthFirstSearchAlgorithm(Algorithm):

    def get_steps(self, initial_state, goal_state):
        state = initial_state
        solution_actions = []
        states = []
        actions = dict()
        actions[state] = []
        while state != goal_state:
            legal_actions = self.get_legal_actions(state)
            for action in legal_actions:
                tmp = self.apply_action(state, action)
                if tmp not in actions:
                    states.append(tmp)
                    tmp_act = solution_actions.copy()
                    tmp_act.append(action)
                    actions[tmp] = tmp_act
            state = states.pop(0)
            solution_actions = actions[state].copy()
        return solution_actions
