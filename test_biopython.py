"""Petit test cam Biopython"""
from io import StringIO
import matplotlib.pyplot as plt
from Bio import Phylo

from src.objet import Node, conversion_newick

A, B, C = Node("A"), Node("B"), Node("C")
D = Node("D", A, B)
racine = Node("root", D, C)

newick = conversion_newick(racine) + ";"
print("Newick :", newick)  # doit renvoyer ((A,B)D,C)root;

arbre = Phylo.read(StringIO(newick), "newick")
Phylo.draw(arbre)  # ouvre une fenêtre avec le dessin
# pour sauvegarder en image à la place :
# Phylo.draw(arbre, do_show=False); plt.savefig("arbre.png")