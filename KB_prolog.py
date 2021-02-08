from pyswip import Prolog

import Emergenza

prolog = Prolog()
prolog.assertz("caserma(caserma_1)")
prolog.assertz("caserma(caserma_2)")
prolog.assertz("caserma(caserma_3)")

prolog.assertz("agenti(caserma_1,30)")
prolog.assertz("agenti(caserma_2,40)")
prolog.assertz("agenti(caserma_3,50)")

prolog.assertz("speciali(caserma_1,10)")
prolog.assertz("speciali(caserma_2,7)")
prolog.assertz("speciali(caserma_3,3)")

# TODO : calcolare il tempo usando A*
prolog.assertz("tempo(caserma_1,5)")
prolog.assertz("tempo(caserma_2,10)")
prolog.assertz("tempo(caserma_3,2)")


#
# print(list(prolog.query("caserma(X), agenti(X, Y), Y > 15, speciali(X,Z), Z > 4, tempo(X,T), T < 6"))[0]["X"])

def findCaserma(emergenza: Emergenza):
    strQuery = "caserma(X), tempo(X,T), agenti(X,Y), speciali(X,Z), veicoli(X,V), T <=" + str(
        emergenza.tempo) + " , Y >=" + str(emergenza.num_agenti) + " , Z>=" + str(
        emergenza.num_speciali) + " , V>=" + str(emergenza.num_veicoli)
    return list(prolog.query(strQuery))[0]["X"]
