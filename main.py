import variables_pieces

echiquier = [] # Tableau représentant l'échiquier

def creer_echiquier(echiquier):
    """Crée un échiquier à l'aide d'un tableau t

    Args:
        echiquier (list): Tableau à 2 dimensions
    """
    for loop in range(19):                             # Répéter 19 fois :
        ligne = []                                         # Tableau ligne dans t
        for loop in range(19):                             # Répéter 19 fois :
                ligne.append(" ")                              # Nouvel indice ayant pour valeur " "
        echiquier.append(ligne)                            # Nouvel indice du tableau t ayant pour valeur un tableau ligne
    for x in range(19):                                # Répéter 19 fois :
        for y in range(19):                                # Répéter 19 fois :
            if y%2 == 0:                                       # Si le reste de y par 2 != à 0 :
                echiquier[x][y] = "|"                              # Dessine quadrillage vertical
                y *= 3                                             # Décalage permettant le quadrillage (Multiplier par 3 à chaque boucle)
            elif x%2 == 0 and echiquier[x][y] == " ":                  # Si le reste de x par 2 != à 0 et que la valeur = " " :
                echiquier[x][y] = "-"                                      # Dessine quadrillage horizontal
    for i in range(8):                                 # Répéter 8 fois :
        i += 1                                             # Ajouter 1 à chaque boucle
        echiquier[i*2-1][1] = 9-i                          # Affiche les coordonnées y (axe des ordonnées) 
        echiquier[17][i*2+1] = chr(ord("A")+i-1)           # Affiche les coordonnées x (axe des abscisses) 
        echiquier[3][i*2+1] = variables_pieces.pion_n      # Dessine Pion Noir
        echiquier[13][i*2+1] = variables_pieces.pion_b     # Dessine Pion Blanc
    echiquier[15][3] = variables_pieces.tour_b         # Dessine Tour Blanche Gauche
    echiquier[15][17] = variables_pieces.tour_b        # Dessine Tour Blanche Droite
    echiquier[15][5] = variables_pieces.cavalier_b     # Dessine Cavalier Blanc Gauche
    echiquier[15][15] = variables_pieces.cavalier_b    # Dessine Cavalier Blanc Droite
    echiquier[15][7] = variables_pieces.fou_b          # Dessine Fou Blanc Gauche
    echiquier[15][13] = variables_pieces.fou_b         # Dessine Fou Blanc Droite
    echiquier[15][9] = variables_pieces.reine_b        # Dessine Reine Blanche
    echiquier[15][11] = variables_pieces.roi_b         # Dessine Roi Blanc
    echiquier[1][3] = variables_pieces.tour_n          # Dessine Tour Noir Gauche
    echiquier[1][17] = variables_pieces.tour_n         # Dessine Tour Noir Droite
    echiquier[1][5] = variables_pieces.cavalier_n      # Dessine Cavalier Noir Gauche
    echiquier[1][15] = variables_pieces.cavalier_n     # Dessine Cavalier Noir Droite
    echiquier[1][7] = variables_pieces.fou_n           # Dessine Fou Noir Gauche
    echiquier[1][13] = variables_pieces.fou_n          # Dessine Fou Noir Droite
    echiquier[1][9] = variables_pieces.roi_n           # Dessine Roi Noir
    echiquier[1][11] = variables_pieces.reine_n        # Dessine Reine Blanche

def tour_joueur():
    joueur1 = input("Nom Joueur 1 : ")             # Demande le nom du joueur 1
    joueur2 = input("Nom Joueur 2 : ")             # Demande le nom du joueur 2
    prochain_tour = joueur1                        # Donne le tour au joueur 1
    if prochain_tour == joueur1:                   # Si le prochain tour est au joueur 1 :
        print(f"C'est le tour de {prochain_tour}")     # Indique à qui est le tour
        prochain_tour = joueur2                        # Donne le tour au joueur 2
    elif prochain_tour == joueur2:                 # Si le prochain tour est au joueur 2 :
        print(f"Tour de {prochain_tour}")              # Indique à qui est le tour
        prochain_tour = joueur1                        # Donne le tour au joueur 1

def afficher_echiquier(echiquier):
    """Affiche l'échiquier

    Args:
        t (list): Tableau à 2 dimensions
    """
    for x in range(19):                     # Répéter 19 fois :
        for y in range(19):                     # Répéter 19 fois :
            print(echiquier[x][y], end=" ")         # Imprimer tableau ligne du tableau t
        print()                                 # Imprimer Saut de ligne
    tour_joueur()                           # Appel de la fonction tour_joueur
    return echiquier                        # Renvoyer t

# TEST :
creer_echiquier(echiquier)    # Crée un échiquier avec les pièces à leur positions par défaut
afficher_echiquier(echiquier) # Affiche l'échiquier sur la console python

dico_coords = {                 # Base de données contenant toutes les coordonnées possibles
    "A":{
        "1": echiquier[15][3],  # A1
        "2": echiquier[13][3],  # A2
        "3": echiquier[11][3],  # A3
        "4": echiquier[9][3],   # A4
        "5": echiquier[7][3],   # A5
        "6": echiquier[5][3],   # A6
        "7": echiquier[3][3],   # A7
        "8": echiquier[1][3]    # A8
    },
    "B":{
        "1": echiquier[15][5],  # B1
        "2": echiquier[13][5],  # B2
        "3": echiquier[11][5],  # B3
        "4": echiquier[9][5],   # B4
        "5": echiquier[7][5],   # B5
        "6": echiquier[5][5],   # B6
        "7": echiquier[3][5],   # B7
        "8": echiquier[1][5]    # B8
    },
    "C":{
        "1": echiquier[15][7],  # C1
        "2": echiquier[13][7],  # C2
        "3": echiquier[11][7],  # C3
        "4": echiquier[9][7],   # C4
        "5": echiquier[7][7],   # C5
        "6": echiquier[5][7],   # C6
        "7": echiquier[3][7],   # C7
        "8": echiquier[1][7]    # C8
    },
    "D":{
        "1": echiquier[15][9],  # D1
        "2": echiquier[13][9],  # D2
        "3": echiquier[11][9],  # D3
        "4": echiquier[9][9],   # D4
        "5": echiquier[7][9],   # D5
        "6": echiquier[5][9],   # D6
        "7": echiquier[3][9],   # D7
        "8": echiquier[1][9]    # D8
    },
    "E":{
        "1": echiquier[15][11], # E1
        "2": echiquier[13][11], # E2
        "3": echiquier[11][11], # E3
        "4": echiquier[9][11],  # E4
        "5": echiquier[7][11],  # E5
        "6": echiquier[5][11],  # E6
        "7": echiquier[3][11],  # E7
        "8": echiquier[1][11]   # E8
    },
    "F":{
        "1": echiquier[15][13], # F1
        "2": echiquier[13][13], # F2
        "3": echiquier[11][13], # F3
        "4": echiquier[9][13],  # F4
        "5": echiquier[7][13],  # F5
        "6": echiquier[5][13],  # F6
        "7": echiquier[3][13],  # F7
        "8": echiquier[1][13]   # F8
    },
    "G":{
        "1": echiquier[15][15], # G1
        "2": echiquier[13][15], # G2
        "3": echiquier[11][15], # G3
        "4": echiquier[9][15],  # G4
        "5": echiquier[7][15],  # G5
        "6": echiquier[5][15],  # G6
        "7": echiquier[3][15],  # G7
        "8": echiquier[1][15]   # G8
    },
    "H":{
        "1": echiquier[15][17], # H1
        "2": echiquier[13][17], # H2
        "3": echiquier[11][17], # H3
        "4": echiquier[9][17],  # H4
        "5": echiquier[7][17],  # H5
        "6": echiquier[5][17],  # H6
        "7": echiquier[3][17],  # H7
        "8": echiquier[1][17]   # H8
    }
}

# TEST :
print(dico_coords["D"]["1"])

def est_majuscule(caractere):
    """Vérifie si un caractère est majuscule ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): True or False
    """
    return "A" <= caractere <= "Z" # Vérifie si l'encodage UTF-8 du caractère est entre A et Z

def est_chiffre(caractere):
    """Vérifie si un caractère est chiffre ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): True of False
    """
    return '0' <= caractere <= '9' # Vérifie si l'encodage UTF-8 du caractère est entre 0 et 9
    
def reco_coordonnees(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): x et y
    
    Returns:
        (list): Dictionnaire à 2 dimensions 
    """
    x = coordonnees[0]       # Attribue le premier caractere de la chaine à la variable x
    y = coordonnees[1]       # Attribue le deuxième caractere de la chaine à la variable y
    est_majuscule(x)         # Vérifie si y est un nombre
    est_chiffre(y)           # Vérifie si y est un chiffre
    return dico_coords[x][y] # Renvoie les indices correspondant aux coordonnées

# TEST :
print(reco_coordonnees("D8"))

def deplacer(x1,y1,x2,y2,t):
    t[x2][y2] = t[x1][y1]
    t[x1][y1] = " "

def deplacement(nom_piece, x1, y1, x2, y2, t):

    if nom_piece == variables_pieces.pion_b:
        
        if x2 == x1-2 and y2 == y1 :        #compare les indices 
            deplacer(x1, y1, x2, y2, t)
        else :
            print("tu ne peut pas déplacer le pion blanc ici") 
    elif nom_piece == variables_pieces.pion_n:
        if x2 == x1+2 and y2 == y1 :        #compare les indices 
            deplacer(x1, y1, x2, y2, t)
        else :
            print("tu ne peut pas déplacer le pion noir ici") 
    #elif nom_piece == variables_pieces.tour_b:
    #elif nom_piece == variables_pieces.tour_n:
    #elif nom_piece == variables_pieces.cavalier_b:
    #elif nom_piece == variables_pieces.cavalier_n:
    #elif nom_piece == variables_pieces.fou_b:
    #elif nom_piece == variables_pieces.fou_n:
    #elif nom_piece == variables_pieces.reine_b:
    #elif nom_piece == variables_pieces.reine_n:
    #elif nom_piece == variables_pieces.roi_b:
    #elif nom_piece == variables_pieces.reine_b:

# TEST :
deplacement(variables_pieces.pion_b, 13, 3, 11,3, echiquier)
# deplacement(variables_pieces.pion_b, 13, 3, 9, 3, echiquier)
afficher_echiquier(echiquier)
