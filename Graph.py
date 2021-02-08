
class Node:
    f: int = 0
    g: int = 0
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

    def connect(self, node1, node2, weight):
        if type(weight).__name__ != "int" and type(weight).__name__ != "float":
            raise Exception("Weight can only be a integer value and not {}".format(type(weight).__name__))
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
            raise Exception("{} - {} is not a valid path".format(node1, node2))

    def pathweight(self, node1, node2):
        if node1 in self.connections and node2 in self.connections:
            # if node1 in self.connections or node2 in self.connections:
            connection1 = self.connections.get(node1)
            if node2 in connection1:
                return connection1.get(node2)
            else:
                raise Exception("{} & {} are not connected".format(node1, node2))
        else:
            raise Exception("{} - {} is not a valid path".format(node1, node2))

    def connection(self, node):
        result = []
        if node in self.connections:
            for connection_nodes in self.connections.get(node):
                result.append(connection_nodes)
            return result
        else:
            return result
            # raise Exception("{} is not a valid node".format(node))

    def connectionmap(self, node):
        if node in self.connections:
            return self.connections.get(node)
        else:
            raise Exception("{} is not a valid node".format(node))

    def nodes(self):
        return self.node

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def euristic(node1, node2):
        return abs(node1.get_x() - node2.get_x()) + abs(node1.get_y() - node2.get_y())

    def min_euristic(self, node):
        minimum = 666
        tempnode = Node(0, 0, 0)
        for noding in self.connections.get(node):
            newmin = self.euristic(node, noding)
            if newmin < minimum:
                tempnode = noding
                minimum = newmin
        return tempnode

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
            if current == goal:
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

def minSearch(list: list()):
    min = Node("", 100, 100)
    min.set_g(9999)
    min.set_h(9999)
    for item in list:
        item: Node()
        if item.f <= min.f:
            min = item
    return min


def printPath(node, path):
    node: Node()
    if node.parent == None:
        path.append(node)
    else:
        printPath(node.parent, path)
        path.append(node)

# def createMap():
#     mappa = Graph()
#     #Nodi standard
#     A = Node("1", 4, 0)
#     B = Node("2", 4, 2)
#     C = Node("3", 6, 1)
#     D = Node("4", 6, 3)
#     E = Node("5", 9, 4)
#     F = Node("6", 7, 5)
#     G = Node("7", 5, 4)
#     H = Node("8", 9, 7)
#     I = Node("9", 7, 6)
#     J = Node("10", 6, 6)
#     K = Node("11", 5, 6)
#     L = Node("12", 4, 8)
#     M = Node("13", 7, 10)
#     N = Node("14", 3, 8)
#     O = Node("15", 2, 9)
#     P = Node("16", 3, 6)
#     Q = Node("17", 0, 7)
#     R = Node("18", 2, 5)
#     S = Node("19", 3, 4)
#     T = Node("20", 0, 5)
#     U = Node("21", 0, 3)
#     W = Node("22", 2, 1)
#
#     #Caserme
#     C1 = Node("Caserma 1", 2,3)
#     C2 = Node("Caserma 2", 7,1)
#     C3 = Node("Caserma 3", 3,10)
#
#     #Aggiungo i nodi alla mappa
#     mappa.addnode(A)
#     mappa.addnode(B)
#     mappa.addnode(C)
#     mappa.addnode(D)
#     mappa.addnode(E)
#     mappa.addnode(F)
#     mappa.addnode(G)
#     mappa.addnode(H)
#     mappa.addnode(I)
#     mappa.addnode(J)
#     mappa.addnode(K)
#     mappa.addnode(L)
#     mappa.addnode(M)
#     mappa.addnode(N)
#     mappa.addnode(O)
#     mappa.addnode(P)
#     mappa.addnode(Q)
#     mappa.addnode(R)
#     mappa.addnode(S)
#     mappa.addnode(T)
#     mappa.addnode(U)
#     mappa.addnode(W)
#     mappa.addnode(C1)
#     mappa.addnode(C2)
#     mappa.addnode(C3)
#
#     #Creo gli archi
#     mappa.connect(A,B,4)
#     mappa.connect(A,C2,1)
#     mappa.connect(A,W,3)
#     mappa.connect(C2,D,3)
#     mappa.connect(C2,E,4)
#     mappa.connect(B,C,3)
#     mappa.connect(C,D,1)
#     mappa.connect(D,E,7)
#     mappa.connect(D,G,4)
#     mappa.connect(E,F,4)
#     mappa.connect(E,H,2)
#     mappa.connect(F,G,6)
#     mappa.connect(G,K,2)
#     mappa.connect(H,I,2)
#     mappa.connect(H,M,1)
#     mappa.connect(I,J,5)
#     mappa.connect(J,K,3)
#     mappa.connect(K,P,3)
#     mappa.connect(K,L,4)
#     mappa.connect(L,N,2)
#     mappa.connect(L,C3,6)
#     mappa.connect(C3,N,5)
#     mappa.connect(C3,M,3)
#     mappa.connect(C3,O,2)
#     mappa.connect(O,N,2)
#     mappa.connect(O,P,3)
#     mappa.connect(O,Q,3)
#     mappa.connect(O,Q,3)
#     mappa.connect(N,P,2)
#     mappa.connect(P,S,2)
#     mappa.connect(S,R,6)
#     mappa.connect(S,W,2)
#     mappa.connect(S,C1,4)
#     mappa.connect(C1,U,4)
#     mappa.connect(U,W,3)
#     mappa.connect(U,T,3)
#     mappa.connect(T,R,2)
#     mappa.connect(T,Q,1)
#     mappa.connect(Q,R,2)
#     return mappa
#
# goal = D
# mappa.a_star(E, goal)
# path = list()
# printPath(goal, path)
#
# for node in path:
#     if node != goal:
#         print(node, end="->")
#     else:
#         print(node)
# print("Costo= " + str(goal.g))
#
# # for item in final_list:
# #     print(item)
