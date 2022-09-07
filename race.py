import functools
from game import Game, play_game
from map import Map
from Players.random_player import RandomPlayer
from Players.searching_player import SearchingPlayer
from search import minimax_search
from node import gen_nodes, gen_matrix, print_matrix
import networkx as nx
import matplotlib.pyplot as plt

cache = functools.lru_cache(10 ** 6)


class Race(Game):
    def __init__(self, n):
        self.nodes = []
        self.initial = self.__construct_map(n)
        self.turn = 0
        

    def __construct_map(self, n):
        matrix = gen_matrix(n)  # genera la matriz de valores (adyacencia)
        # matrix = [
        #     [0, 71, 0, 0, 0],
        #     [71, 0, 0, 20, 55],
        #     [0, 0, 0, 0, 41],
        #     [0, 20, 0, 0, 0],
        #     [0, 55, 41, 0, 0],
        # ]
        print_matrix(matrix)  # Muestra en pantalla lo que hay en la matriz (para debug)
        self.nodes = gen_nodes(n)  # Genera una lista de nodos
        #print_nodes(self.nodes)  # Imprime los valores de los nodos
        # Se recorre la lista de nodos para buscar las conexiones de los nodos basandose en la matriz de adyacencia
        for node in self.nodes:
            for second_node in self.nodes:
                if matrix[node.n_id][second_node.n_id] != 0:
                    node.connections.append((second_node, matrix[node.n_id][second_node.n_id]))

        self.nodes[len(self.nodes) - 1].set_final(True)
        plays = [('j1', self.nodes[0].name)]
        ini_map = Map(self.nodes[0], 'j1', 0, dict(j1=0, j2=0), plays)

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
    #draw graph
    def draw_graph(self, state):
        camino = []
        for i in state.plays:
            camino.append(i[1])
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node.name)
            for connection in node.connections:
                G.add_edge(node.name, connection[0].name, weight=connection[1])
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='black', width=1, alpha=0.7)
        for i in range(0,len(camino)-1):
            if i%2 == 0:
                nx.draw_networkx_edges(G,pos,edgelist=[(camino[i],camino[i+1])],width=8,alpha=0.5,edge_color='r')
            else:
                nx.draw_networkx_edges(G,pos,edgelist=[(camino[i],camino[i+1])],width=8,alpha=0.5,edge_color='b')
        plt.show()
        

depth = 10
game = Race(10)
players = dict(j1=SearchingPlayer(minimax_search, depth), j2=SearchingPlayer(minimax_search, depth))
path = play_game(game, players, verbose=True)
game.draw_graph(path)