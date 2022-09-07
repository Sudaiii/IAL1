class Map:
    def __init__(self, start_node, to_move, turn, points, plays):
        self.current_node = start_node
        self.to_move = to_move
        self.turn = turn
        self.points = points
        self.plays = plays
        self.utility = 0

    def __str__(self):
        return str(self.current_node) + ' ' + str(self.utility) + ' ' + str(self.to_move)
