"""étapes de la réconciliation :
  1. associer chaque feuille de G à une feuille de E  -> remplir projection(feuilles)
  2. parcourir G des feuilles vers la racine          -> remplir projection(g) avec LCA
  3. déduire spéciation ou duplication pour noeuds internes
"""
from src.lca import findLCA

##############Etape1

def est_feuille(noeud):
    """si pas de fils droit et pas de fils gauche alors c'est une feuille"""
    return noeud.left is None and noeud.right is None

def espece_de(nom_gene):
    """Trouve l'espece d'un nom de gène. exemple : gène 'Humain_2' = 'Humain' """
    espece = nom_gene.split("_")[0]
    return espece

def associer_feuilles(g, feuilles_E):
    """Étape 1 : proj(feuille de G) = feuille de E de la même espèce. """
    if est_feuille(g):
        espece_de_g = espece_de(g.data)
        g.projection = feuilles_E[espece_de_g]
        g.evenement = "feuille"
    else:
        associer_feuilles(g.left, feuilles_E)
        associer_feuilles(g.right, feuilles_E)


##############Etape 2

def remonter_arbre_genes(g, E):
    """Calcule projection(g) et le type d'événement de chaque nœud interne de G"""

    # base : une feuille a déjà sa projection (calculé étape précédente).
    if est_feuille(g):
        return

    # on traite les deux enfants
    remonter_arbre_genes(g.left, E)
    remonter_arbre_genes(g.right, E)

    # on récupère leurs proj (noeuds de E).
    proj_gauche = g.left.projection
    proj_droite = g.right.projection

    # projction(g) = dernier ancêtre commun (lca) de ces deux noeuds dans E.
    ancetre = findLCA(E, proj_gauche, proj_droite)
    g.projection = ancetre

    # determine duplication ou spéciation 
    if ancetre is proj_gauche:
        g.evenement = "duplication"
    elif ancetre is proj_droite:
        g.evenement = "duplication"
    else:
        g.evenement = "spéciation"

    # Affichage au fur et a mesure
    print("%s : enfants proj = (%s, %s) -> LCA = %s -> %s"
          % (g.data, proj_gauche.data, proj_droite.data, ancetre.data, g.evenement))


##############Lancer étapes

def reconcilier(G, E, feuilles_E):
    """Lance les étapes 1 et 2 sur l'arbre de gènes G."""
    associer_feuilles(G, feuilles_E)
    remonter_arbre_genes(G, E)

def afficher_annotations(g):
    """Affiche proj et l'événement de chaque nœud de G (enfants d'abord)"""
    if not est_feuille(g):
        afficher_annotations(g.left)
        afficher_annotations(g.right)
    print("  %-10s Projection = %-6s  %s" % (g.data, g.projection.data, g.evenement))