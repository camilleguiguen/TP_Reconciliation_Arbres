"""Étape 3 : compter les pertes de gènes.

Idée : sur chaque arête g -> h de l'arbre de gènes G, le gène « traverse »
dans l'arbre d'espèces E tous les nœuds situés entre projection(g) et
projection(h). À chaque nœud traversé, la lignée du gène choisit UN fils ;
l'autre fils n'a pas reçu de descendant du gène : c'est une PERTE.

Exception : si g est une SPECIATION, la première traversée (celle qui part de
projection(g)) est « utilisée » par l'autre enfant de g, donc rien n'est perdu.
Pour une duplication, les deux copies restent dans la même espèce : toutes
les traversées comptent.
"""
from src.reconciliation import est_feuille


def chemin_vers(depart, cible):
    """Chemin dans E de `depart` (en haut) jusqu'à `cible` (en bas).
    Renvoie la liste des nœuds [depart, ..., cible], ou None si `cible`
    n'est pas sous `depart`.  (On descend, car les nœuds de E n'ont pas de parent.)"""
    if depart is None:
        return None
    if depart is cible:                      # on est arrivé
        return [depart]
    for fils in (depart.left, depart.right):
        reste = chemin_vers(fils, cible)
        if reste is not None:                # la cible est dans ce sous-arbre
            return [depart] + reste
    return None                              # la cible n'est pas ici


def frere_de(parent, enfant):
    """Dans E : l'autre fils de `parent` (celui qui n'est pas `enfant`)."""
    if parent.left is enfant:
        return parent.right
    return parent.left


def pertes_sur_arete(g, h):
    """Liste des nœuds de E perdus sur l'arête g -> h (du BAS vers le HAUT,
    ordre attendu par le dessin)."""
    chemin = chemin_vers(g.projection, h.projection)
    if chemin is None:
        raise ValueError("projection(%s) n'est pas sous projection(%s) : "
                         "réconciliation incohérente" % (h.data, g.data))
    perdus = []
    # on regarde chaque pas (x -> y) du chemin, en partant du haut
    for i in range(len(chemin) - 1):
        x = chemin[i]
        y = chemin[i + 1]
        premier_pas = (i == 0)               # le pas qui part de projection(g)
        if premier_pas and g.evenement == "spéciation":
            continue                         # le frère est occupé par l'autre enfant de g
        perdus.append(frere_de(x, y))        # sinon : le frère de y est perdu
    perdus.reverse()                         # on veut du bas vers le haut
    return perdus


def calculer_pertes(g):
    """Remplit l'attribut `pertes` de chaque nœud de G (sauf la racine)
    et renvoie le nombre total de pertes."""
    if est_feuille(g):
        return 0
    total = 0
    for h in (g.left, g.right):
        h.pertes = pertes_sur_arete(g, h)
        total = total + len(h.pertes)
    total = total + calculer_pertes(g.left) + calculer_pertes(g.right)
    return total