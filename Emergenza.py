import Map

# quando genero un'emergenza casuale creo un oggetto emergenza per salvare l'intervento richiesto
class Emergency:
    grado: int
    tempo: int
    num_agenti: int
    num_speciali: int
    num_veicoli: int

    def __init__(self):
        self.grado = 0
        self.tempo = 0
        self.num_agenti = 0
        self.num_speciali = 0
        self.num_veicoli = 0

    def __init__(self, grado, tempo, num_agenti, num_speciali, num_veicoli, luogo: Map.Node):
        self.grado = grado
        self.tempo = tempo
        self.num_agenti = num_agenti
        self.num_speciali = num_speciali
        self.num_veicoli = num_veicoli
        self.luogo = luogo

    def __str__(self):
        string = "\nE' STATA PREDETTA UN'EMERGENZA DI GRADO " + str(self.grado) + ":\n\n" \
              "Tempo richiesto per l'intervento: <= " + str(self.tempo) +" min\n" \
              "Numero agenti richiesti per l'intervento: >= " + str(self.num_agenti) + "\n"\
              "Numero agenti speciali richiesti per l'intervento: >= " + str(self.num_speciali) + "\n"\
              "Numero veicoli richiesti per l'intervento: >= " + str(self.num_veicoli) + "\n"
        return string
