from Players.player import Player

# Jugador que escoge jugadas en base a un algoritmo,
# inspirado por codigo del GitHub del libro Artificial Intelligence: A Modern Approach (games4e.ipynb)
class SearchingPlayer(Player):
    def __init__(self, algorithm, max_depth):
        super().__init__()
        self.algorithm = algorithm
        self.max_depth = max_depth

    def move(self, game, state):
        return self.algorithm(game, state, self.max_depth)[1]
