import Map

class Emergenza:

    tempo : int
    num_agenti : int
    num_speciali : int
    num_veicoli : int

    def __init__(self):
        self.tempo = 0
        self.num_agenti = 0
        self.num_speciali = 0
        self.num_veicoli = 0

    def __init__(self, tempo, num_agenti, num_speciali, num_veicoli, luogo : Map.Node):
        self.tempo = tempo
        self.num_agenti = num_agenti
        self.num_speciali = num_speciali
        self.num_veicoli = num_veicoli
        self.luogo = luogo

