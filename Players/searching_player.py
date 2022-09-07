from Players.player import Player


class SearchingPlayer(Player):
    def __init__(self, algorithm, max_depth):
        super().__init__()
        self.algorithm = algorithm
        self.max_depth = max_depth

    def move(self, game, state):
        return self.algorithm(game, state, self.max_depth)[1]
