import time
import pygame
from math import log, sqrt
from random import choice

#główna cześć algorytmu bazująca na innych implementacjach jeszcze będę ją analizował czy mogę coś zrobić lepiej/inaczej/bardziej po swojemu
#muszę uzupełnić jeszcze ruchy dla figur

class Stat(object):
    __slots__ = ('value', 'visits')

    def __init__(self, value=0.0, visits=0):
        self.value = value
        self.visits = visits

    def __repr__(self):
        return u"Stat(value={}, visits={})".format(self.value, self.visits)


class UCT(object):
    def __init__(self):
        self.history = []
        self.stats = {}

        self.max_depth = 0
        self.data = {}
        # na podstawie przykładu narazie uzupełnione
        self.calculation_time = float(5)
        self.max_actions = int(1000)
        self.C = float(1.4)

    #def legal_actions(self, state):

    #def next_state(self, history, action):

    #def current_player(self, state):

    #def previous_player(self, state):

    #def is_ended(self, state):

    #def end_values(self, state):

    def update(self, state):
        self.history.append(state)

    def get_action(self):
        self.max_depth = 0
        self.data = {'C': self.C, 'max_actions': self.max_actions, 'name': self.name}
        self.stats.clear()

        state = self.history[-1]
        player = self.current_player(state)
        legal = self.legal_actions(state)

        games = 0
        begin = time.time()
        while time.time() - begin < self.calculation_time:
            self.run_simulation()
            games += 1

        self.data.update(games=games, max_depth=self.max_depth, time=str(time.time() - begin))
        print(self.data['games'], self.data['time'])
        print("Maximum depth searched:", self.max_depth)

        self.data['actions'] = self.calculate_action_values(self.history, player, legal)
        action = self.data['actions'][0]['action']
        new_state = self.next_state(self.history, action)
        self.update(new_state)
        for m in self.data['actions']:
            print(self.action_template.format(**m))

        return action

    def run_simulation(self):
        C, stats = self.C, self.stats

        visited_states = []
        history_copy = self.history[:]
        state = history_copy[-1]

        expand = True
        for t in range(1, self.max_actions + 1):
            legal = self.legal_actions(state)
            actions_states = [(a, self.next_state(history_copy, a)) for a in legal]

            if expand and not all(S in stats for a, S in actions_states):
                stats.update((S, Stat()) for a, S in actions_states if S not in stats)
                expand = False
                if t > self.max_depth:
                    self.max_depth = t

            if expand:
                actions_states = [(a, S, stats[S]) for a, S in actions_states]
                log_total = log(sum(e.visits for a, S, e in actions_states) or 1)
                values_actions = [
                    (a, S, (e.value / (e.visits or 1)) + C * sqrt(log_total / (e.visits or 1)))
                    for a, S, e in actions_states
                ]
                max_value = max(v for _, _, v in values_actions)
                actions_states = [(a, S) for a, S, v in values_actions if v == max_value]
                action, state = choice(actions_states)
                visited_states.append(state)
                history_copy.append(state)

                if self.is_endend(state):
                    break
            end_values = self.end_values(state)
            for state in visited_states:
                if state not in stats:
                    continue
                S = stats[state]
                S.visits += 1
                S.values += end_values[self.previus_player(state)]


class UCTWins(UCT):
    name = "jrb.mcts.uct"
    action_template = "{action}: {percent:.2f}% ({wins} / {plays})"

    def __init__(self):
        super(UCTWins, self).__init__()

    def calculate_action_values(self, history, player, legal):
        actions_states = ((a, self.next_state(history, a)) for a in legal)
        return sorted(
            ({'action': a,
              'percent': 100 * self.stats[S].value / (self.stats[S].visits or 1),
              'wins': self.stats[S].value,
              'plays': self.stats[S].visits}
             for a, S in actions_states),
            key=lambda x: (x['percent'], x['plays']),
            reverse=True
        )
