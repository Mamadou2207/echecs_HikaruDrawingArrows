def creer_echiquier():
    t = []                                    # Tableau t
    for loop in range(19):                    # Répéter 19 fois :
        ligne = []                                # Tableau ligne dans t
        for loop in range(19):                    # Répéter 19 fois :
                ligne.append(" ")                     # Nouvel indice ayant pour valeur " "
        t.append(ligne)                           # Nouvel indice ayant pour valeur un tableau ligne
    for x in range(19):                       # Répéter 19 fois :
        for y in range(19):                       # Répéter 19 fois :
            if y%2 == 0:                              # Si le reste de y par 2 != à 0 :
                t[x][y] = "|"                             # Dessine quadrillage vertical
                y *= 3                                    # Décalage permettant le quadrillage (Multiplier par 3 à chaque boucle)
            elif x%2 == 0 and t[x][y] == " ":         # Si le reste de x par 2 != à 0 et que la valeur = " " :
                t[x][y] = "-"                             # Dessine quadrillage horizontal
    for i in range(8):                        # Répéter 8 fois :
        i += 1                                    # Ajouter 1 à chaque boucle
        t[i*2-1][1] = 9-i                         # Affiche les coordonnées y (axe des ordonnées) 
        t[17][i*2+1] = chr(ord("A")+i-1)          # Affiche les coordonnées x (axe des abscisses) 
        t[3][i*2+1] = "♟︎"                        # Dessine Pion Noir
        t[13][i*2+1] = "♙"                       # Dessine Pion Blanc
    t[15][3] = "♖"                           # Dessine Tour Blanche Gauche
    t[15][17] = "♖"                          # Dessine Tour Blanche Droite
    t[15][5] = "♘"                           # Dessine Cavalier Blanc Gauche
    t[15][15] = "♘"                          # Dessine Cavalier Blanc Droite
    t[15][7] = "♗"                           # Dessine Fou Blanc Gauche
    t[15][13] = "♗"                          # Dessine Fou Blanc Droite
    t[15][9] = "♕"                           # Dessine Reine Blanche
    t[15][11] = "♔"                          # Dessine Roi Blanc
    t[1][3] = "♜"                            # Dessine Tour Noir Gauche
    t[1][17] = "♜"                           # Dessine Tour Noir Droite
    t[1][5] = "♞"                            # Dessine Cavalier Noir Gauche
    t[1][15] = "♞"                           # Dessine Cavalier Noir Droite
    t[1][7] = "♝"                            # Dessine Fou Noir Gauche
    t[1][13] = "♝"                           # Dessine Fou Noir Droite
    t[1][9] = "♚"                            # Dessine Roi Noir
    t[1][11] = "♛"                           # Dessine Reine Blanche
    for x in range(19):                       # Répéter 19 fois :
        for y in range(19):                       # Répéter 19 fois :
            print(t[x][y], end=" ")                   # Imprimer tableau ligne du tableau t
        print()                                   # Imprimer Saut de ligne
    return t                                  # Renvoyer t
