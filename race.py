import functools
from operator import index
from game import Game, play_game
from map import Map
from Players.random_player import RandomPlayer
from Players.searching_player import SearchingPlayer
from search import minimax_search, alphabeta_search
from node import gen_nodes, gen_matrix, print_matrix
import networkx as nx
import matplotlib.pyplot as plt

cache = functools.lru_cache(10 ** 6)

# El juego implementado
# Se basa en la interfaz Game
depth = 0
algorithms = ""


class Race(Game):
    def __init__(self, n):
        self.nodes = []
        self.initial = self.__construct_map(n)
        self.turn = 0
        self.print_prunings = ""
        

        

    # Construye el estado inicial
    def __construct_map(self, n):
        matrix = gen_matrix(n)  # genera la matriz de valores (adyacencia)
        self.nodes = gen_nodes(n)  # Genera una lista de nodos
        # Se recorre la lista de nodos para buscar las conexiones de los nodos basandose en la matriz de adyacencia
        for node in self.nodes:
            for second_node in self.nodes:
                if matrix[node.n_id][second_node.n_id] != 0:
                    node.connections.append((second_node, matrix[node.n_id][second_node.n_id]))
        

        print_matrix(self.nodes, matrix)
        value_start, value_finish, value_depth,algorithm, pruning = input_data()
        global depth
        depth = value_depth
        
        #modify global variable
        global algorithms
        algorithms = algorithm

        self.print_prunings = pruning
        print(self.print_prunings)
        self.nodes[value_start].set_start(True)

        self.nodes[value_finish].set_final(True)

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
    #dibuja el grafo dado un estado
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
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='black', width=1, alpha=0.7)
        #alterna los colores de las rutas que tomo cada jugador. Max = Rojo , Min = Azul 
        for i in range(0,len(camino)-1):
            if i%2 == 0:
                nx.draw_networkx_edges(G,pos,edgelist=[(camino[i],camino[i+1])],width=8,alpha=0.5,edge_color='r')
            else:
                nx.draw_networkx_edges(G,pos,edgelist=[(camino[i],camino[i+1])],width=8,alpha=0.5,edge_color='b')
        plt.show()
    

        


#Entradas de datos con sus respectivas comprobaciones
def input_data():
    node_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    #Validacion de entrada nodo inicial
    flag = True
    while flag:
        try:
            txt_start = input("Ingrese nombre del nodo INICIAL [A-J]: ")
            txt_start = txt_start.upper()
            if (len(txt_start) > 1) or (len(txt_start)==0) or (txt_start not in node_list):
                raise
            else:
                flag = False
                start = node_list.index(txt_start)
        except:
            print("Favor de ingresar una entrada valida\n")

    #Validacion de entrada nodo final       
    flag = True
    while flag:
        try:
            txt_finish = input("Ingrese nombre del nodo FINAL [A-J]: ")
            txt_finish = txt_finish.upper()
            if (len(txt_finish) > 1) or (len(txt_finish)==0) or (txt_finish not in node_list):
                raise
            elif node_list.index(txt_finish) == start:
                print("El nodo elegido debe ser diferente al nodo de salida\n")
            else:
                flag = False
                finish = node_list.index(txt_finish)
        except:
            print("Favor de ingresar una entrada valida\n")

    #Validacion de entrada profundidad de busqueda
    flag = True
    while flag:
        try:
           depth_value = int(input("Ingrese nivel máximo a comprobar del arbol para MiniMax [número mayor a 0]: "))
           if (depth_value>0):
                flag = False
        except:
            print("Favor de ingresar una entrada valida\n")

    #validacion de entrada de algoritmo a usar
    flag = True
    while flag:
        try:
            txt_algorithm = input("Ingrese algoritmo a usar [minimax, alphabeta]: ")
            txt_algorithm = txt_algorithm.lower()
            if (txt_algorithm != "minimax") and (txt_algorithm != "alphabeta"):
                raise
            else:
                flag = False
                algorithm = txt_algorithm
        except:
            print("Favor de ingresar una entrada valida\n")
    
    #validacion de entrada para mostrar o no la poda alphabeta
    flag = True
    while flag:
        try:
            txt_pruning = input("¿Desea mostrar la poda de AlphaBeta? [si, no]: ")
            txt_pruning = txt_pruning.lower()
            if (txt_pruning != "si") and (txt_pruning != "no"):
                raise
            else:
                flag = False
                pruning = txt_pruning
        except:
            print("Favor de ingresar una entrada valida\n")

    return start, finish, depth_value, algorithm , pruning


# Main del programa
game = Race(10) #llama a que la matriz de juego sea de 10x10

if algorithms  == "minimax":
    players = dict(j1=SearchingPlayer(minimax_search, depth), j2=SearchingPlayer(minimax_search, depth))
else:
    players = dict(j1=SearchingPlayer(alphabeta_search, depth), j2=SearchingPlayer(alphabeta_search, depth))
    
state = play_game(game, players, verbose=True)
game.draw_graph(state)
