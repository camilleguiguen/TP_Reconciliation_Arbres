"""Exemple de test : les mammifères (Humain, Souris, Chat).

voir Figure 1 rapport latex.
"""
from src.objet import Node


def exemple_HSC():
    """Renvoie (G, E, feuilles_E, attendu)."""

    # --- Arbre d'espèces S = ((Humain,Souris),Chat) ---
    humain = Node("Humain")
    souris = Node("Souris")
    chat = Node("Chat")
    hs = Node("HS", humain, souris)        # ancêtre Humain + Souris
    E = Node("Rac", hs, chat)             # racine de E

    # --- Arbre de gènes G = ((Humain_2,Chat_2),Souris_1) ---
    humain_2 = Node("Humain_2")
    chat_2 = Node("Chat_2")
    souris_1 = Node("Souris_1")
    g2 = Node("g2", humain_2, chat_2)
    G = Node("g1", g2, souris_1)           # racine de G

    # nom d'espèce -> nœud (feuille) de E
    feuilles_E = {"Humain": humain, "Souris": souris, "Chat": chat}

    # Résultat correct attendu à comparer avec mes resultats ---
    attendu = {
        "projection": {"Humain_2": "Humain", "Chat_2": "Chat", "Souris_1": "Souris", "g2": "Rac", "g1": "Rac"},
        # type d'événement des nœuds internes de G
        "evenement": {"g2": "spéciation", "g1": "duplication"},
        "duplications": 1,
        "speciations": 1,
        "pertes": 3,
    }

    
    return G, E, feuilles_E, attendu