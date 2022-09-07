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
    node_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # Se crean 10 nombres de nodes
    nodes = []
    for i in range(0, n):
        nodes.append(Node(node_list[i], i))
    return nodes


def print_nodes(nodes):
    for node in nodes:
        print(node.name + " id: " + str(node.n_id) + " s: " + str(node.start) + " f: "
              + str(node.final) + " vA: " + str(node.plays))


# ====================Mat

def empty_matrix(n):
    matrix_row = list()
    for i in range(0, n):
        matrix_col = list()
        for j in range(0, n):
            matrix_col.append(0)
        matrix_row.append(matrix_col)
    return matrix_row


def gen_matrix(n):
    matrix = empty_matrix(n)
    for i in range(0, n):
        for j in range(0, n):
            if j < i and random.randint(0, 1) == 0:
                matrix[i][j] = random.randint(0, 100)
                matrix[j][i] = matrix[i][j]
    return matrix


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


# n = 5  # tamaño de la matriz
# matrix = gen_matrix(n)  # genera la matriz de valores (adyacencia)
# print_matrix(matrix)  # Muestra en pantalla lo que hay en la matriz (para debug)
# nodes = gen_nodes(n)  # Genera una lista de nodos
# print_nodes(nodes)  # Imprime los valores de los nodos
# for node in nodes:  # Se recorre la lista de nodos para buscar las conexiones de los nodos basandose en la matriz de adyacencia
#     node.search_connections(matrix)
#
# print("Conexiones")
# for node in nodes:
#     print("nodo " + node.name + " : ", end="")
#     print(node.connections)
#     # En las tuplas el primer valor es el nombre del nodo, el segundo el indice en matriz y el tercero es el peso que cuesta llegar a ese nodo
#     # (nombre, indice, costo para llegar)