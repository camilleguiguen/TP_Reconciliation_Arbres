"""Affichages et comptages finaux (bilan de la réconciliation)."""
from src.reconciliation import est_feuille


def compter_evenements(g, bilan=None):
    """Compte spéciations, duplications et pertes dans tout l'arbre de G"""
    if bilan is None:
        bilan = {"speciations": 0, "duplications": 0, "pertes": 0}
    bilan["pertes"] = bilan["pertes"] + len(g.pertes)
    if not est_feuille(g):
        if g.evenement == "duplication":
            bilan["duplications"] = bilan["duplications"] + 1
        else:
            bilan["speciations"] = bilan["speciations"] + 1
        compter_evenements(g.left, bilan)
        compter_evenements(g.right, bilan)
    return bilan


def afficher_noeuds(g):
    """Affiche pour chaque noeud de G : projection, événement, pertes sur l'arête."""
    if not est_feuille(g):
        afficher_noeuds(g.left)
        afficher_noeuds(g.right)
    noms_pertes = [x.data for x in g.pertes]
    texte = "  %-9s projection = %-8s %-11s" % (g.data, g.projection.data, g.evenement)
    if noms_pertes:
        texte = texte + " pertes sur l'arête au-dessus : " + ", ".join(noms_pertes)
    print(texte)