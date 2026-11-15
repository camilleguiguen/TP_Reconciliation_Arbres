"""structure d'arbre inspiré de struct node de l'algo recurssif findLCA() 

celle de base :  
struct node {
    int data; 
    struct node *left; 
    struct node *right; 
};

mes ajouts :
projection et evenement
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data         # nom / étiquette du noeud
        self.left = left         # fils gauche
        self.right = right       # fils droit
        self.projection = None   # noeud de E associé au gène de G
        self.evenement = None    # "feuille", "spéciation", "duplication"
        self.pertes = []         # noeuds de E perdus sur l'arête parent -> ce nœud

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