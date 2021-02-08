# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# list.append(input("Inserisci numero criminali"))
# list.append(input("Inserisci tipo di armi"))
# list.append(input("C'è stata un'esplosione?"))
# list.append(input("C'è stata un'aggressione?"))
# list.append(input("C'è stata una rapina?"))
# list.append(input("C'è stata un furto?"))
# list.append(input("C'è stata una sommossa?"))
# list.append(input("Ci sono feriti?"))


# Press the green button in the gutter to run the script.

import random as random
from Classifier import classify
from Map import Node
from Map import Graph
from Emergenza import Emergency as Emergenza

def createMap():
    mappa = Graph()
    # Nodi standard
    A = Node("1", 4, 0)
    B = Node("2", 4, 2)
    C = Node("3", 6, 1)
    D = Node("4", 6, 3)
    E = Node("5", 9, 4)
    F = Node("6", 7, 5)
    G = Node("7", 5, 4)
    H = Node("8", 9, 7)
    I = Node("9", 7, 6)
    J = Node("10", 6, 6)
    K = Node("11", 5, 6)
    L = Node("12", 4, 8)
    M = Node("13", 7, 10)
    N = Node("14", 3, 8)
    O = Node("15", 2, 9)
    P = Node("16", 3, 6)
    Q = Node("17", 0, 7)
    R = Node("18", 2, 5)
    S = Node("19", 3, 4)
    T = Node("20", 0, 5)
    U = Node("21", 0, 3)
    W = Node("22", 2, 1)

    # Caserme
    C1 = Node("Caserma 1", 2, 3)
    C2 = Node("Caserma 2", 7, 1)
    C3 = Node("Caserma 3", 3, 10)

    # Aggiungo i nodi alla mappa
    mappa.addnode(A)
    mappa.addnode(B)
    mappa.addnode(C)
    mappa.addnode(D)
    mappa.addnode(E)
    mappa.addnode(F)
    mappa.addnode(G)
    mappa.addnode(H)
    mappa.addnode(I)
    mappa.addnode(J)
    mappa.addnode(K)
    mappa.addnode(L)
    mappa.addnode(M)
    mappa.addnode(N)
    mappa.addnode(O)
    mappa.addnode(P)
    mappa.addnode(Q)
    mappa.addnode(R)
    mappa.addnode(S)
    mappa.addnode(T)
    mappa.addnode(U)
    mappa.addnode(W)
    mappa.addnode(C1)
    mappa.addnode(C2)
    mappa.addnode(C3)

    # Creo gli archi
    mappa.connect(A, B, 4)
    mappa.connect(A, C2, 1)
    mappa.connect(A, W, 3)
    mappa.connect(C2, D, 3)
    mappa.connect(C2, E, 4)
    mappa.connect(B, C, 3)
    mappa.connect(C, D, 1)
    mappa.connect(D, E, 7)
    mappa.connect(D, G, 4)
    mappa.connect(E, F, 4)
    mappa.connect(E, H, 2)
    mappa.connect(F, G, 6)
    mappa.connect(G, K, 2)
    mappa.connect(H, I, 2)
    mappa.connect(H, M, 1)
    mappa.connect(I, J, 5)
    mappa.connect(J, K, 3)
    mappa.connect(K, P, 3)
    mappa.connect(K, L, 4)
    mappa.connect(L, N, 2)
    mappa.connect(L, C3, 6)
    mappa.connect(C3, N, 5)
    mappa.connect(C3, M, 3)
    mappa.connect(C3, O, 2)
    mappa.connect(O, N, 2)
    mappa.connect(O, P, 3)
    mappa.connect(O, Q, 3)
    mappa.connect(O, Q, 3)
    mappa.connect(N, P, 2)
    mappa.connect(P, S, 2)
    mappa.connect(S, R, 6)
    mappa.connect(S, W, 2)
    mappa.connect(S, C1, 4)
    mappa.connect(C1, U, 4)
    mappa.connect(U, W, 3)
    mappa.connect(U, T, 3)
    mappa.connect(T, R, 2)
    mappa.connect(T, Q, 1)
    mappa.connect(Q, R, 2)
    return mappa

def create_situation():
    X_Input = [[]]
    list = []
    print("Creo emergenza casuale:")
    list.append(random.randint(0, 4))
    print("NUMERO CRIMINALI:")
    if list.__getitem__(0) == 0:
        print("E' stato generato 0: ci sono da 0 a 3 criminali")
    elif list.__getitem__(0) == 1:
        print("E' stato generato 1: ci sono da 4 a 7 criminali")
    elif list.__getitem__(0) == 2:
        print("E' stato generato 2: ci sono da 8 a 11 criminali")
    elif list.__getitem__(0) == 3:
        print("E' stato generato 3: ci sono da 12 a 14 criminali")
    elif list.__getitem__(0) == 4:
        print("E' stato generato 4: ci sono più di 15 criminali")
    print("")

    list.append(random.randint(0, 2))
    print("ARMI:")
    if list.__getitem__(1) == 0:
        print("E' stato generato 0: non ci sono armi")
    elif list.__getitem__(1) == 1:
        print("E' stato generato 1: ci sono armi bianche")
    elif list.__getitem__(1) == 2:
        print("E' stato generato 2: ci sono armi da fuoco")
    print("")

    list.append(random.randint(0, 1))
    print("ESPLOSIONE:")
    if list.__getitem__(2) == 0:
        print("E' stato generato 0: non è avvenuta un'esplosione")
    if list.__getitem__(2) == 1:
        print("E' stato generato 1: è avvenuta un'esplosione")
    print("")

    list.append(random.randint(0, 1))
    print("AGGRESSIONE:")
    if list.__getitem__(3) == 0:
        print("E' stato generato 0: non è avvvenuta un'aggressione")
    if list.__getitem__(3) == 1:
        print("E' stato generato 1: è avvenuta un'aggressione")
    print("")

    list.append(random.randint(0, 1))
    print("RAPINA:")
    if list.__getitem__(4) == 0:
        print("E' stato generato 0: non è avvvenuta una rapina")
    if list.__getitem__(4) == 1:
        print("E' stato generato 1: è avvenuta una rapina")
    print("")

    list.append(random.randint(0, 1))
    print("FURTO:")
    if list.__getitem__(5) == 0:
        print("E' stato generato 0: non è avvvenuta un furto")
    if list.__getitem__(5) == 1:
        print("E' stato generato 1: è avvenuta un furto")
    print("")

    list.append(random.randint(0, 1))
    print("SOMMOSSA:")
    if list.__getitem__(6) == 0:
        print("E' stato generato 0: non è avvvenuta una sommossa")
    if list.__getitem__(6) == 1:
        print("E' stato generato 1: è avvenuta una sommossa")
    print("")

    list.append(random.randint(0, 1))
    print("FERITI:")
    if list.__getitem__(7) == 0:
        print("E' stato generato 0: non ci sono feriti")
    if list.__getitem__(7) == 1:
        print("E' stato generato 1: ci sono feriti")
    print("")

    X_Input = [list]
    return X_Input

def random_node():
    return random.randint(1, 22)

def classification(x, node):
    print("")
    print("")
    if x == 1:
        Emergenza(1, 25, 2, 0, 1, node)
        print("E' STATA PREDETTA UN'EMERGENZA DI GRADO 1:")
        print("")
        print("Tempo richiesto per l'intervento: <= 25 min")
        print("Numero agenti richiesti per l'intervento: >= 2")
        print("Numero agenti speciali richiesti per l'intervento: >= 0")
        print("Numero veicoli richiesti per l'intervento: >= 1")

    elif x == 2:
        Emergenza(2, 20, 4, 0, 2, node)
        print("E' STATA PREDETTA UN'EMERGENZA DI GRADO 2:")
        print("")
        print("Tempo richiesto per l'intervento: <= 20 min")
        print("Numero agenti richiesti per l'intervento: >= 4")
        print("Numero agenti speciali richiesti per l'intervento: >= 0")
        print("Numero veicoli richiesti per l'intervento: >= 2")

    elif x == 3:
        Emergenza(3, 15, 8, 2, 4, node)
        print("E' STATA PREDETTA UN'EMERGENZA DI GRADO 3:")
        print("")
        print("Tempo richiesto per l'intervento: <= 15 min")
        print("Numero agenti richiesti per l'intervento: >= 8")
        print("Numero agenti speciali richiesti per l'intervento: >= 2")
        print("Numero veicoli richiesti per l'intervento: >= 4")

    elif x == 4:
        Emergenza(4, 10, 15, 6, 10, node)
        print("E' STATA PREDETTA UN'EMERGENZA DI GRADO 4:")
        print("")
        print("Tempo richiesto per l'intervento: <= 10 min")
        print("Numero agenti richiesti per l'intervento: >= 15")
        print("Numero agenti speciali richiesti per l'intervento: >= 6")
        print("Numero veicoli richiesti per l'intervento: >= 10")

    elif x == 5:
        Emergenza(5, 5, 25, 10, 15, node)
        print("E' STATA PREDETTA UN'EMERGENZA DI GRADO 5:")
        print("")
        print("Tempo richiesto per l'intervento: <= 5 min")
        print("Numero agenti richiesti per l'intervento: >= 25")
        print("Numero agenti speciali richiesti per l'intervento: >= 10")
        print("Numero veicoli richiesti per l'intervento: >= 15")

if __name__ == '__main__':
    mappa = createMap()
    nodo = random_node()
    input = create_situation()
    print(input)
    print(main(input))
    pred = main(input)
    print(classification(pred, nodo))

