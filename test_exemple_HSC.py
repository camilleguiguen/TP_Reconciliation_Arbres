"""Teste l'exemple des mammifères : affichage des arbres et vérifications LCA.
Lancer :  python3 test_exemple_HSC.py
"""
from src.dessiner_arbres import conversion_newick
from src.lca import findLCA
from src.exemple_HSC import exemple_HSC


def dessiner(newick, fichier):
    """Dessine un arbre avec Biopython (attention : ignoré si absent)"""
    try:
        from io import StringIO
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from Bio import Phylo
    except ImportError:
        print("  (Biopython/matplotlib absents : pas de dessin)")
        return
    arbre = Phylo.read(StringIO(newick), "newick")
    Phylo.draw(arbre, do_show=False)
    plt.savefig(fichier)
    plt.close()
    print("  dessin enregistré :", fichier)


G, E, feuilles_E, attendu = exemple_HSC()

# dessiner les arbres avec Biopython
print("Arbre d'espèces E :", conversion_newick(E) + ";")
dessiner(conversion_newick(E) + ";", "arbre_especes.png")
print("Arbre de gènes G  :", conversion_newick(G) + ";")
dessiner(conversion_newick(G) + ";", "arbre_genes.png")

# Vérification du LCA sur l'arbre d'espèces
print("\nTests LCA sur E :")
hu = feuilles_E["Humain"]
so = feuilles_E["Souris"]
ch = feuilles_E["Chat"]
assert findLCA(E, hu, so).data == "HS"
assert findLCA(E, hu, ch).data == "Rac"
assert findLCA(E, so, ch).data == "Rac"
assert findLCA(E, hu, hu) is hu      # même nœud = duplication
print("  OK")

# Résultat attendu de la réconciliation (pour plus tard)
print("\nRésultat attendu de la réconciliation :")
for nom, m in attendu["projection"].items():
    print("  M(%s) = %s" % (nom, m))
for nom, ev in attendu["evenement"].items():
    print("  %s : %s" % (nom, ev))
print("  duplications = %d, spéciations = %d, pertes = %d"
      % (attendu["duplications"], attendu["speciations"], attendu["pertes"]))