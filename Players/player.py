class Player:
    def __init__(self):
        self.points = 0

    def move(self, game, state):
        """Return a collection of the allowable moves from this state."""
        raise NotImplementedError
