import random
from Players.player import Player

# Jugador que escoge jugadas al azar,
# inspirado por codigo del GitHub del libro Artificial Intelligence: A Modern Approach (games4e.ipynb)
class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self, game, state):
        return random.choice(list(game.actions(state)))
