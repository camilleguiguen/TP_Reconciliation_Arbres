# TP Phylogénie Bioinfo avancée- Réconciliation arbre de gènes / arbre d'espèces (modèle DL)

## Téléchargement depuis github
git clone https://github.com/camilleguiguen/TP_Reconciliation_Arbres.git

## A installer (facultatif)
biopython
matplotlib

```bash
pip install biopython matplotlib
```
Si vous utilisez une version spécifique de Python:
```bash
pip3 install biopython matplotlib
```

## Lancement du code sur exemple_HSC
```bash
python3 main.py 
```

## Différents fichiers de code
- `src/objet.py` : objet Node pour représenter les noeuds des arbres
- `src/lca.py`   : algorithme LCA (version récursive du cours)

- `src/reconciliation.py` : étape 1 (traiter feuilles) et étape 2 (remonter l'arbre de gènes)
- `src/pertes.py` : étape 3 (compter les pertes de gènes)

- `src/bilan.py` : affichages et comptages finaux (bilan de la réconciliation) 
- `src/dessiner_arbres.py` : conversion_newick + fonction Biopython pour afficher les arbres

- `src/exemple_HSC.py` : exemple de test correspondant à la figure 1 du rapport (Humain, Souris, Chat)