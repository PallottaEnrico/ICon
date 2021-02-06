from pyswip import Prolog
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

# TODO: impostare i vincoli secondo il grado di emergenza
print(list(prolog.query("caserma(X), agenti(X, Y), Y > 15, speciali(X,Z), Z > 4, tempo(X,T), T < 6"))[0]["X"])