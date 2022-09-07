import random
from Players.player import Player


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self, game, state):
        return random.choice(list(game.actions(state)))
