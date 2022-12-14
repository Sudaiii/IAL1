import random


# Clase que representa una ciudad del mapa de juego
class Node:
    def __init__(self, name, n_id):  # Constructor
        self.name = name
        self.start = False
        self.final = False
        self.n_id = n_id
        self.connections = []

    def set_start(self, start):
        self.start = start

    def set_final(self, final):
        self.final = final

    def search_connections(self, matrix):
        # Lista para saber el nombre del nodo en base a letras
        node_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for i in range(0, len(matrix)):
            if matrix[self.n_id][i] != 0:
                self.connections.append((node_list[i], i, matrix[self.n_id][i]))

    def __str__(self):
        return self.name


# ===================Nodos=====================

def gen_nodes(n):
    node_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # Se crean 10 nombres de nodos
    nodes = []
    for i in range(0, n):
        nodes.append(Node(node_list[i], i))
    return nodes

# ====================Matriz =======================


# Genera matriz vacía
def empty_matrix(n):
    matrix_row = list()
    for i in range(0, n):
        matrix_col = list()
        for j in range(0, n):
            matrix_col.append(0)
        matrix_row.append(matrix_col)
    return matrix_row


# Rellena la matriz con valores aleatorios
def gen_matrix(n):
    matrix = empty_matrix(n)
    for i in range(0, n):
        for j in range(0, n):
            if j < i and random.randint(0, 1) == 0:
                matrix[i][j] = random.randint(0, 100)
                matrix[j][i] = matrix[i][j]
    return matrix


# Muestra matriz por pantalla
def print_matrix(nodes, matrix):
    print("==========Matriz generada para la carrera=========")
    print(f"{' ':<3}", end=" ")
    for node in nodes:
        print(f"{node.name:<3}", end=" ")
    print()
    for i in range(0,
                   len(matrix)):
        print(f"{nodes[i].name:<3}", end=" ")
        for j in range(0,
                       len(matrix)):
            print(f"{matrix[i][j]:<3}", end=" ")
        print()
