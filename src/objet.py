"""structure d'arbre inspiré de struct node de l'algo recurssif findLCA() 

celle de base :  
struct node {
    int data; 
    struct node *left; 
    struct node *right; 
};

mes ajouts :
projection, evenement et pertes
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data         # nom / étiquette du noeud
        self.left = left         # fils gauche
        self.right = right       # fils droit
        self.projection = None   # noeud de E associé au gène de G
        self.evenement = None    # "feuille", "spéciation", "duplication"
        self.pertes = []         # noeuds de E perdus sur l'arête parent -> ce nœud
