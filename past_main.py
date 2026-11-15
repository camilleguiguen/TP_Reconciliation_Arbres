"""Construit un petit arbre, teste le LCA, affiche l'abre avec Biopython."""
from src.objet import Node, conversion_newick
from src.lca import findLCA
from io import StringIO
import matplotlib.pyplot as plt
from Bio import Phylo

# Noeuds pour tester le code
A = Node("A")
B = Node("B")
C = Node("C")
AB = Node("AB", A, B)
ABC = Node("ABC", AB, C)

print()
# pour chaque couple, l'algo LCA trouve la meilleure parcimonie
for (x, y) in [(A, B), (A, C), (B, C), (A, A), (A, AB)]:
    res = findLCA(ABC, x, y)
    print("LCA(%s, %s) = %s" % (x.data, y.data, res.data))

# on converti en chaine de newick pour pouvoir afficher l'arbre avec biopython
chaine_newick = conversion_newick(ABC)
print("Arbre (Newick) :", chaine_newick + ";")

# dessine l'arbre
Phylo.draw(Phylo.read(StringIO(chaine_newick), "newick"))


