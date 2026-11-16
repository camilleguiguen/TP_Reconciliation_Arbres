from src.reconciliation import est_feuille


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


# ---------------------------------------------------------------
# Dessin de l'arbre de gènes RECONCILIE (événements + pertes)
# ---------------------------------------------------------------
COULEURS = {"duplication": "red", "spéciation": "blue", "perte": "gray",
            "feuille": "black"}


def construire_clade(g):
    """Transforme le sous-arbre de g en Clade Biopython (récursif)."""
    from Bio.Phylo.BaseTree import Clade

    if est_feuille(g):
        clade = Clade(branch_length=1, name=g.data, color=COULEURS["feuille"])
    else:
        enfants = [construire_clade(g.left), construire_clade(g.right)]
        clade = Clade(branch_length=1,
                      name="%s : %s" % (g.data, g.evenement),
                      clades=enfants,
                      color=COULEURS[g.evenement])

    # Pertes sur l'arête qui arrive en g : chaque perte est une petite
    # branche grise accrochée au-dessus de g (du bas vers le haut).
    for espece_perdue in getattr(g, "pertes", []):
        feuille_perte = Clade(branch_length=1,
                              name="perte (%s)" % espece_perdue.data,
                              color=COULEURS["perte"])
        clade = Clade(branch_length=1, clades=[clade, feuille_perte],
                      color=COULEURS["spéciation"])
    return clade


def dessiner_reconciliation(G, fichier="arbres/reconciliation.png"):
    """Dessine l'arbre de gènes réconcilié et l'enregistre en PNG."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
        from Bio import Phylo
        from Bio.Phylo.BaseTree import Tree
    except ImportError:
        print("Biopython/matplotlib absents : pas de dessin "
              "(pip install biopython matplotlib).")
        return

    arbre = Tree(root=construire_clade(G), rooted=True)

    fig = plt.figure(figsize=(9, 5))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(arbre, axes=ax, do_show=False,
               label_func=lambda c: c.name if c.name else "")
    legende = [Line2D([0], [0], color=COULEURS["duplication"], lw=3, label="duplication"),
               Line2D([0], [0], color=COULEURS["spéciation"], lw=3, label="spéciation"),
               Line2D([0], [0], color=COULEURS["perte"], lw=3, label="perte")]
    ax.legend(handles=legende, loc="lower left")
    ax.set_title("Arbre de gènes réconcilié")
    fig.savefig(fichier, bbox_inches="tight")
    plt.close(fig)
    print("Dessin enregistré :", fichier)