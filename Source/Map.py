class Node:
    # Euristica + Distanza Stimata
    f: int = 0
    # Valore Euristica
    g: int = 0
    # Distanza stimata
    h: int = 0

    def __init__(self, value, x, y):
        self.parent = None
        self.value = value
        self.x = x
        self.y = y

    def set_parent(self, node):
        self.parent = node

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_val(self):
        return self.value

    def is_same(self, node):
        return self.value == node.value

    def set_g(self, value):
        self.g = value
        self.set_f()

    def set_h(self, value):
        self.h = value
        self.set_f()

    def set_f(self):
        self.f = self.g + self.h

    def __str__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self.node = []
        self.connections = {}

    def addnode(self, node):
        self.node.append(node)

    # connette due nodi con arco avente peso passato come argomento
    def connect(self, node1, node2, weight):
        if type(weight).__name__ != "int" and type(weight).__name__ != "float":
            raise Exception("Peso non valido".format(type(weight).__name__))
        if node1 in self.node and node2 in self.node:
            if node1 in self.connections:
                all_nodes = self.connections.get(node1)
                all_nodes[node2] = weight
            else:
                self.connections[node1] = {node2: weight}
            # Utile solo se il grafo non è orientato--------------------
            if node2 in self.connections:
                all_nodes = self.connections.get(node2)
                all_nodes[node1] = weight
            else:
                self.connections[node2] = {node1: weight}
            # -----------------------------------------------------------
        else:
            raise Exception("L'arco non è valido".format(node1, node2))

    # ritorna peso di arco tra due nodi
    def pathweight(self, node1, node2):
        if node1 in self.connections and node2 in self.connections:
            connection1 = self.connections.get(node1)
            if node2 in connection1:
                return connection1.get(node2)
            else:
                raise Exception("I due nodi non sono connessi".format(node1, node2))
        else:
            raise Exception("L'arco non e' valido".format(node1, node2))

    # ritorna una lista di nodi adiacienti a node
    def connection(self, node):
        result = []
        if node in self.connections:
            for connection_nodes in self.connections.get(node):
                result.append(connection_nodes)
            return result
        else:
            return result

    def nodes(self):
        return self.node

    def __str__(self):
        return self.__class__.__name__

    # Euristica di Manhattan
    @staticmethod
    def euristic(node1, node2):
        return abs(node1.get_x() - node2.get_x()) + abs(node1.get_y() - node2.get_y())

    def a_star(self, start, goal):

        if start not in self.connections or goal not in self.connections:
            raise Exception("Non sono stati forniti nodi validi.")

        open_list = list()
        start.set_g(0)
        start.set_h(self.euristic(start, goal))
        closed_list = list()
        open_list.append(start)

        while len(open_list) != 0:
            current = minSearch(open_list)
            open_list.remove(current)
            if current.is_same(goal):
                break
            successor: Node
            for successor in self.connection(current):
                successor_current_cost = current.g + self.pathweight(current, successor)
                if successor in open_list:
                    if successor.g <= successor_current_cost:
                        break
                elif successor in closed_list:
                    if successor.g <= successor_current_cost:
                        continue
                else:
                    open_list.append(successor)
                    successor.set_h(self.euristic(successor, goal))
                successor.set_g(successor_current_cost)
                successor.set_parent(current)
            closed_list.append(current)


# metodo che data una lista restituisce il nodo avente il parametro f minimo (euristica + distanza stimata)
def minSearch(list: list()):
    min = Node("", 100, 100)
    min.set_g(9999)
    min.set_h(9999)
    for item in list:
        item: Node()
        if item.f <= min.f:
            min = item
    return min


# stampo il percorso trovato per arrivare al nodo destinazione
def printPath(node, path):
    node: Node()
    if node.parent == None:
        path.append(node)
    else:
        printPath(node.parent, path)
        path.append(node)
