import random as random
from Classifier import classify
from Map import Node, printPath
from Map import Graph
from Emergenza import Emergency
from pyswip import Prolog


def createKB():
    kb = Prolog()
    kb.assertz("caserma(caserma_1)")
    kb.assertz("caserma(caserma_2)")
    kb.assertz("caserma(caserma_3)")

    kb.assertz("agenti(caserma_1,30)")
    kb.assertz("agenti(caserma_2,40)")
    kb.assertz("agenti(caserma_3,50)")

    kb.assertz("speciali(caserma_1,10)")
    kb.assertz("speciali(caserma_2,7)")
    kb.assertz("speciali(caserma_3,3)")

    kb.assertz("veicoli(caserma_1,7)")
    kb.assertz("veicoli(caserma_2,20)")
    kb.assertz("veicoli(caserma_3,13)")
    return kb


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
    mappa.connect(A, B, 6)
    mappa.connect(A, C2, 3)
    mappa.connect(A, W, 5)
    mappa.connect(C2, D, 5)
    mappa.connect(C2, E, 6)
    mappa.connect(B, C, 5)
    mappa.connect(C, D, 3)
    mappa.connect(D, E, 9)
    mappa.connect(D, G, 6)
    mappa.connect(E, F, 6)
    mappa.connect(E, H, 4)
    mappa.connect(F, G, 8)
    mappa.connect(G, K, 4)
    mappa.connect(H, I, 4)
    mappa.connect(H, M, 3)
    mappa.connect(I, J, 7)
    mappa.connect(J, K, 5)
    mappa.connect(K, P, 5)
    mappa.connect(K, L, 6)
    mappa.connect(L, N, 4)
    mappa.connect(L, C3, 8)
    mappa.connect(C3, N, 7)
    mappa.connect(C3, M, 5)
    mappa.connect(C3, O, 4)
    mappa.connect(O, N, 4)
    mappa.connect(O, P, 5)
    mappa.connect(O, Q, 5)
    mappa.connect(O, Q, 5)
    mappa.connect(N, P, 4)
    mappa.connect(P, S, 4)
    mappa.connect(S, R, 8)
    mappa.connect(S, W, 4)
    mappa.connect(S, C1, 6)
    mappa.connect(C1, U, 6)
    mappa.connect(U, W, 5)
    mappa.connect(U, T, 5)
    mappa.connect(T, R, 4)
    mappa.connect(T, Q, 3)
    mappa.connect(Q, R, 4)
    return mappa


def create_event():
    X_Input = [[]]
    list = []
    print("---------------------------EMERGENZA---------------------------")
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
    # print("")

    list.append(random.randint(0, 2))
    print("ARMI:")
    if list.__getitem__(1) == 0:
        print("E' stato generato 0: non ci sono armi")
    elif list.__getitem__(1) == 1:
        print("E' stato generato 1: ci sono armi bianche")
    elif list.__getitem__(1) == 2:
        print("E' stato generato 2: ci sono armi da fuoco")
    # print("")

    list.append(random.randint(0, 1))
    print("ESPLOSIONE:")
    if list.__getitem__(2) == 0:
        print("E' stato generato 0: non è avvenuta un'esplosione")
    if list.__getitem__(2) == 1:
        print("E' stato generato 1: è avvenuta un'esplosione")
    # print("")

    list.append(random.randint(0, 1))
    print("AGGRESSIONE:")
    if list.__getitem__(3) == 0:
        print("E' stato generato 0: non è avvvenuta un'aggressione")
    if list.__getitem__(3) == 1:
        print("E' stato generato 1: è avvenuta un'aggressione")
    # print("")

    list.append(random.randint(0, 1))
    print("RAPINA:")
    if list.__getitem__(4) == 0:
        print("E' stato generato 0: non è avvvenuta una rapina")
    if list.__getitem__(4) == 1:
        print("E' stato generato 1: è avvenuta una rapina")
    # print("")

    list.append(random.randint(0, 1))
    print("FURTO:")
    if list.__getitem__(5) == 0:
        print("E' stato generato 0: non è avvvenuta un furto")
    if list.__getitem__(5) == 1:
        print("E' stato generato 1: è avvenuta un furto")
    # print("")

    list.append(random.randint(0, 1))
    print("SOMMOSSA:")
    if list.__getitem__(6) == 0:
        print("E' stato generato 0: non è avvvenuta una sommossa")
    if list.__getitem__(6) == 1:
        print("E' stato generato 1: è avvenuta una sommossa")
    # print("")

    list.append(random.randint(0, 1))
    print("FERITI:")
    if list.__getitem__(7) == 0:
        print("E' stato generato 0: non ci sono feriti")
    if list.__getitem__(7) == 1:
        print("E' stato generato 1: ci sono feriti")
    # print("")
    X_Input = [list]

    place = random_place(mappa)
    print("LUOGO:")
    print("Evento avvenuto nel luogo: " + str(place))
    print("---------------------------------------------------------------")
    return place, X_Input


def random_place(mappa: Graph):
    return mappa.nodes()[random.randint(0, 21)]


# specifica per ogni grado di emergenza [1,2,3,4,5] le risorse di cui ha bisogno
def classification(x, node):
    if x == 1:
        e = Emergency(1, 25, 2, 0, 1, node)
    elif x == 2:
        e = Emergency(2, 20, 4, 0, 2, node)
    elif x == 3:
        e = Emergency(3, 15, 8, 2, 4, node)
    elif x == 4:
        e = Emergency(4, 10, 15, 6, 10, node)
    elif x == 5:
        e = Emergency(5, 5, 25, 10, 15, node)
    return e


if __name__ == '__main__':
    # Viene generata la mappa della città
    mappa = createMap()

    #Creo la base di conoscenza
    kb = createKB()

    # Genero un evento casuale per cui si richiede un intevento
    place, event = create_event()

    # Predizione del grado di emergenza per l'evento generato
    prediction = classify(event, "DataSet2.csv")

    # Determino per il grado generato le risorse di cui ha bisogno
    emergency = classification(prediction, place)
    print(emergency)

    # Determino il tempo che ogni caserma impiega ad arrivare sul luogo dell'evento e aggiungo l'informazione alla KB
    mappa.a_star(mappa.nodes()[-3], place)
    kb.assertz("tempo(caserma_1," + str(place.g) + ")")
    mappa.a_star(mappa.nodes()[-2], place)
    kb.assertz("tempo(caserma_2," + str(place.g) + ")")
    mappa.a_star(mappa.nodes()[-1], place)
    kb.assertz("tempo(caserma_3," + str(place.g) + ")")

    # Interrogo la base di conoscenza affinché indichi quale/i caserma/e può intervenire soddisfacendo le richieste dell'emergenza
    strQuery = "caserma(X), tempo(X,T), agenti(X,Y), speciali(X,Z), veicoli(X,V), T<" + str(emergency.tempo+1) + ", Y >=" + str(emergency.num_agenti) + " , Z>=" + str(
        emergency.num_speciali) + " , V>=" + str(emergency.num_veicoli)
    result = list(kb.query(strQuery))

    # Stampa le caserme che possono intervenire
    print("Sono abilitate ad intervenire le caserme:")
    for item in result:
        print(item["X"])

