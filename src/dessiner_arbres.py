def conversion_newick(noeud):
    """renvoie chaîne Newick de l'arbre pour pouvoir faire un arbre biopython"""
    # cas de base : une feuille, on renvoie juste son nom
    if noeud.left is None and noeud.right is None:
        return noeud.data

    # général : on convertit fils gauche et fils droit
    gauche = conversion_newick(noeud.left)
    droite = conversion_newick(noeud.right)

    # return (gauche,droite)nom
    return "(" + gauche + "," + droite + ")" + noeud.data


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
