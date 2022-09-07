import functools
from game import Game, play_game
from map import Map
from Players.random_player import RandomPlayer
from Players.searching_player import SearchingPlayer
from search import minimax_search, alphabeta_search
from node import gen_nodes, gen_matrix, print_matrix

cache = functools.lru_cache(10 ** 6)

# El juego implementado
# Se basa en la interfaz Game
class Race(Game):
    def __init__(self, n):
        self.initial = self.__construct_map(n)
        self.turn = 0

    # Construye el estawdo inicial
    @staticmethod
    def __construct_map(n):
        matrix = gen_matrix(n)  # genera la matriz de valores (adyacencia)
        print_matrix(matrix)  # Muestra en pantalla lo que hay en la matriz (para debug)
        nodes = gen_nodes(n)  # Genera una lista de nodos
        # print_nodes(nodes)  # Imprime los valores de los nodos
        # Se recorre la lista de nodos para buscar las conexiones de los nodos basandose en la matriz de adyacencia
        for node in nodes:
            for second_node in nodes:
                if matrix[node.n_id][second_node.n_id] != 0:
                    node.connections.append((second_node, matrix[node.n_id][second_node.n_id]))

        nodes[0].set_start(True)

        nodes[len(nodes) - 1].set_final(True)

        plays = [('j1', nodes[0].name)]
        ini_map = Map(nodes[0], 'j1', 0, dict(j1=0, j2=0), plays)

        return ini_map

    def actions(self, state):
        candidates = []
        for candidate in state.current_node.connections:
            if (state.to_move, candidate[0].name) not in state.plays:
                candidates.append(candidate)
        return candidates

    def result(self, state, move):
        self.turn += 1
        active_player = state.to_move
        state = Map(move[0], 'j2' if active_player == 'j1' else 'j1', state.turn + 1, state.points, state.plays.copy())
        state.plays.append((active_player, move[0].name))
        state.points[active_player] += move[1]
        state.utility = (state.points['j1'] if active_player == 'j1' else -state.points['j1'])
        return state

    def is_terminal(self, state):
        return len(self.actions(state)) == 0 or state.current_node.final

    def utility(self, state, player):
        return state.utility if player == 'j1' else -state.utility


# Main del programa
depth = 2
game = Race(10)
players = dict(j1=SearchingPlayer(alphabeta_search, depth), j2=SearchingPlayer(alphabeta_search, depth))
play_game(game, players, verbose=True)
