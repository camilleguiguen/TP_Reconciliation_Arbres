"""Réconciliation d'un arbre de gènes avec un arbre d'espèces (modèle DL).
Lancer :  python3 main.py 
"""
from src.reconciliation import associer_feuilles, remonter_arbre_genes
from src.pertes import calculer_pertes
from src.bilan import compter_evenements, afficher_noeuds
from src.dessiner_arbres import dessiner_reconciliation
from src.exemple_HSC import exemple_HSC

def reconcilier(titre, G, E, feuilles_E, attendu, fichier_dessin):
    print("=" * 66)
    print(titre)
    print("=" * 66)

    print("\nÉtape 1 : association des feuilles de G aux feuilles de E")
    associer_feuilles(G, feuilles_E)

    print("Étape 2 : remontée dans l'arbre de gènes (LCA)")
    remonter_arbre_genes(G, E)

    print("Étape 3 : comptage des pertes")
    calculer_pertes(G)

    print("\nRésultat, nœud par nœud (enfants d'abord) :")
    afficher_noeuds(G)

    bilan = compter_evenements(G)
    print("\nBilan :")
    print("  spéciations  :", bilan["speciations"])
    print("  duplications :", bilan["duplications"])
    print("  pertes       :", bilan["pertes"])
    print("  coût DL (duplications + pertes) :",
          bilan["duplications"] + bilan["pertes"])

    # Comparaison avec le résultat attendu
    if all(bilan[k] == attendu[k] for k in ("speciations", "duplications", "pertes")):
        print("  -> conforme au résultat attendu")
    else:
        print("  -> ATTENTION : différent de l'attendu", attendu)

    dessiner_reconciliation(G, fichier_dessin)
    print()


G, E, feuilles_E, attendu = exemple_HSC()
reconcilier("Exemple 1 : Humain, Souris, Chat", G, E, feuilles_E, attendu,
            "arbres/reconciliation_HSC.png")