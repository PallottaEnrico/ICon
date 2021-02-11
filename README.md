# Progetto ICon
**Studenti**:<br>
Mattia Palano, Enrico Pallotta
## Come eseguire
Il software è sviluppato interamente in python.<br>
Per testare il software è necessario eseguire il file main.py . <br>
***Attenzione***: Il software utilizza la libreria *pyswip*, per poter utilizzare tale libreria è necessario aver installato [swi-prolog](https://www.swi-prolog.org/Download.html). <br>
Per visualizzare la presentazione clicca [qui](Presentazione.pdf)
## Descrizione
Il software simula una situazione in cui si verifica un crimine ed è necessario l'intervento da parte di una **caserma**.<br>
Il classificatore prenderà in input un evento generato casualmente secondo 8 features e darà in output il grado di emergenza associato all'evento.<br>
L'algoritmo a* determinerà per ogni caserma il tempo richiesto per arrivare sul luogo dell'evento e inserirà tali valori in una **KB** rappresentata in **Prolog**. <br>
Una interrogazione alla base di conoscenza determinerà quali sono le caserme in grado di intervenire secondo le necessità di ciascun grado di emergenza descritte di seguito.
### Emergenza
Ogni grado di emergenza imporrà delle richieste relative a:
1. Tempestività con la quale bisogna intervenire (espressa in minuti)
2. Numero di agenti ordinari necessari
3. Numero di agenti speciali necessari
4. Numero di veicoli necessari

#### Emergenza 1 :
1. Tempo <= 25
2. Numero agenti >= 2
3. Numero agenti speciali >= 0
4. Numero veicoli >= 1
#### Emergenza 2 :
1. Tempo <= 20
2. Numero agenti >= 4
3. Numero agenti speciali >= 0
4. Numero veicoli >= 2
#### Emergenza 3 :
1. Tempo <= 15
2. Numero agenti >= 8
3. Numero agenti speciali >= 2
4. Numero veicoli >= 4
#### Emergenza 4 :
1. Tempo <= 10
2. Numero agenti >= 15
3. Numero agenti speciali >= 6
4. Numero veicoli >= 10
#### Emergenza 5 :
1. Tempo <= 5
2. Numero agenti >= 25
3. Numero agenti speciali >= 10
4. Numero veicoli >= 15