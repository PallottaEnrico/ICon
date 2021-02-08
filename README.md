# ICon
Il classificatore prenderà in input un evento generato casualmente e darà in output il grado di emergenza associato all'evento<br>
### Emergenza
Ogni grado di emergenza imporrà delle richieste relative a:
1. Tempestività con la quale bisogna intervenire (espressa in minuti)
2. Numero di agenti ordinari necessari
3. Numero di agenti speciali necessari
4. Numero di veicoli necessari

### Gradi di emergenza
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