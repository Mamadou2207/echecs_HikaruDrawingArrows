def creer_echiquier():
    """
    Crée un tableau de valeurs de l'échiquier.
    """
    echiquier = [
        [""] * 8 for _ in range(8)  # Créer un tableau vide de 8x8
    ]
    # Placer les pièces sur l'échiquier
    echiquier[0] = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]  # Ligne supérieure pour les pièces noires
    echiquier[1] = ["♟"] * 8  # Pions noirs
    echiquier[2] = [" "] * 8  # Pions case vide
    echiquier[3] = echiquier[2] 
    echiquier[4] = echiquier[2]
    echiquier[5] = echiquier[2]
    echiquier[6] = ["♙"] * 8  # Pions blancs
    echiquier[7] = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]  # Ligne inférieure pour les pièces blanches
    return echiquier

def afficher_echiquier(echiquier):
    taille = 8
    
    # Afficher les indices de colonne
    print("   " + "  " + chr(ord('a') + i) for i in range(taille))
    
    # Afficher la ligne de séparation
    print("  +" + "---+" * taille)
    
    # Afficher l'échiquier avec les pièces et les lignes de séparation
    for i in range(taille):
        print(f"{taille - i} |", end=" ")  # Afficher les indices de ligne (j'ai mis end pour ne pas qu'il y ait de saut de ligne entre colonnes => affichage plus compact)
        for j in range(taille):
            print(echiquier[i][j] + " |", end=" ")
        print()
        print("  +" + "---+" * taille)  # Afficher la ligne de séparation

# Appeler la fonction pour créer l'échiquier
echiquier = creer_echiquier()

# Afficher l'échiquier
afficher_echiquier(echiquier)
