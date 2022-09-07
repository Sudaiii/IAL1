import math
import functools
cache = functools.lru_cache(10**6)
infinity = math.inf


def minimax_search(game, state, max_depth):
    """Search game tree to determine best move; return (value, move) pair."""
    player = state.to_move

    def max_value(state, last_move):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if state.turn == max_depth:
            return game.utility(state, player), last_move
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), a)
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(state, last_move):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if state.turn == max_depth:
            return game.utility(state, player), last_move
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), a)
            if v2 < v:
                v, move = v2, a
        return v, move

    return max_value(state, None)


def alphabeta_search(game, state, max_depth):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move

    def max_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    def min_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity)
