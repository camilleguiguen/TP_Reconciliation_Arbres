"""Teste les premières étapes de la réconciliation sur l'exemple des mammifères.
Lancer :  python3 test_reconciliation.py
"""
from src.exemple_HSC import exemple_HSC
from src.reconciliation import reconcilier, afficher_annotations, est_feuille

G, S, feuilles_S, attendu = exemple_HSC()

reconcilier(G, S, feuilles_S)

print("Résultat :")
afficher_annotations(G)


# --- Comparaison avec le résultat attendu ---
def verifier(g):
    assert g.projection.data == attendu["projection"][g.data], g.data
    if not est_feuille(g):
        assert g.evenement == attendu["evenement"][g.data], g.data
        verifier(g.left)
        verifier(g.right)

verifier(G)
print("\nToutes les projections et événements correspondent à l'attendu.")