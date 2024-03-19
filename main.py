import variables_pieces

t = [] # Tableau représentant l'échiquier

def creer_echiquier(t):
    """Crée un échiquier à l'aide d'un tableau t

    Args:
        t (list): Tableau à 2 dimensions
    """
    for loop in range(19):                     # Répéter 19 fois :
        ligne = []                                 # Tableau ligne dans t
        for loop in range(19):                     # Répéter 19 fois :
                ligne.append(" ")                      # Nouvel indice ayant pour valeur " "
        t.append(ligne)                            # Nouvel indice du tableau t ayant pour valeur un tableau ligne
    for x in range(19):                        # Répéter 19 fois :
        for y in range(19):                        # Répéter 19 fois :
            if y%2 == 0:                               # Si le reste de y par 2 != à 0 :
                t[x][y] = "|"                              # Dessine quadrillage vertical
                y *= 3                                     # Décalage permettant le quadrillage (Multiplier par 3 à chaque boucle)
            elif x%2 == 0 and t[x][y] == " ":          # Si le reste de x par 2 != à 0 et que la valeur = " " :
                t[x][y] = "-"                              # Dessine quadrillage horizontal
    for i in range(8):                         # Répéter 8 fois :
        i += 1                                     # Ajouter 1 à chaque boucle
        t[i*2-1][1] = 9-i                          # Affiche les coordonnées y (axe des ordonnées) 
        t[17][i*2+1] = chr(ord("A")+i-1)           # Affiche les coordonnées x (axe des abscisses) 
        t[3][i*2+1] = variables_pieces.pion_n      # Dessine Pion Noir
        t[13][i*2+1] = variables_pieces.pion_b     # Dessine Pion Blanc
    t[15][3] = variables_pieces.tour_b         # Dessine Tour Blanche Gauche
    t[15][17] = variables_pieces.tour_b        # Dessine Tour Blanche Droite
    t[15][5] = variables_pieces.cavalier_b     # Dessine Cavalier Blanc Gauche
    t[15][15] = variables_pieces.cavalier_b    # Dessine Cavalier Blanc Droite
    t[15][7] = variables_pieces.fou_b          # Dessine Fou Blanc Gauche
    t[15][13] = variables_pieces.fou_b         # Dessine Fou Blanc Droite
    t[15][9] = variables_pieces.reine_b        # Dessine Reine Blanche
    t[15][11] = variables_pieces.roi_b         # Dessine Roi Blanc
    t[1][3] = variables_pieces.tour_n          # Dessine Tour Noir Gauche
    t[1][17] = variables_pieces.tour_n         # Dessine Tour Noir Droite
    t[1][5] = variables_pieces.cavalier_n      # Dessine Cavalier Noir Gauche
    t[1][15] = variables_pieces.cavalier_n     # Dessine Cavalier Noir Droite
    t[1][7] = variables_pieces.fou_n           # Dessine Fou Noir Gauche
    t[1][13] = variables_pieces.fou_n          # Dessine Fou Noir Droite
    t[1][9] = variables_pieces.roi_n           # Dessine Roi Noir
    t[1][11] = variables_pieces.reine_n        # Dessine Reine Blanche

def tour_joueur():
    joueur1 = input("Nom Joueur 1 : ")
    joueur2 = input("Nom Joueur 2 : ")
    prochain_tour = joueur1
    if prochain_tour == joueur1:
        print(f"C'est le tour de {prochain_tour}")
        prochain_tour = joueur2

    elif prochain_tour == joueur2:
        print(f"Tour de {prochain_tour}")
        prochain_tour = joueur1

def afficher_echiquier(t):
    """Affiche l'échiquier

    Args:
        t (list): Tableau à 2 dimensions
    """
    for x in range(19):             # Répéter 19 fois :
        for y in range(19):             # Répéter 19 fois :
            print(t[x][y], end=" ")         # Imprimer tableau ligne du tableau t
        print()                         # Imprimer Saut de ligne
    tour_joueur()                   # Appel de la fonction tour_joueur
    return t                        # Renvoyer t

# TEST :
creer_echiquier(t)    # Crée un échiquier avec les pièces à leur positions par défaut
afficher_echiquier(t) # Affiche l'échiquier sur la console python

dico_coords = {         # Base de données contenant toutes les coordonnées possibles
    "A":{
        "1": t[15][3],  # A1
        "2": t[13][3],  # A2
        "3": t[11][3],  # A3
        "4": t[9][3],   # A4
        "5": t[7][3],   # A5
        "6": t[5][3],   # A6
        "7": t[3][3],   # A7
        "8": t[1][3]    # A8
    },
    "B":{
        "1": t[15][5],  # B1
        "2": t[13][5],  # B2
        "3": t[11][5],  # B3
        "4": t[9][5],   # B4
        "5": t[7][5],   # B5
        "6": t[5][5],   # B6
        "7": t[3][5],   # B7
        "8": t[1][5]    # B8
    },
    "C":{
        "1": t[15][7],  # C1
        "2": t[13][7],  # C2
        "3": t[11][7],  # C3
        "4": t[9][7],   # C4
        "5": t[7][7],   # C5
        "6": t[5][7],   # C6
        "7": t[3][7],   # C7
        "8": t[1][7]    # C8
    },
    "D":{
        "1": t[15][9],  # D1
        "2": t[13][9],  # D2
        "3": t[11][9],  # D3
        "4": t[9][9],   # D4
        "5": t[7][9],   # D5
        "6": t[5][9],   # D6
        "7": t[3][9],   # D7
        "8": t[1][9]    # D8
    },
    "E":{
        "1": t[15][11], # E1
        "2": t[13][11], # E2
        "3": t[11][11], # E3
        "4": t[9][11],  # E4
        "5": t[7][11],  # E5
        "6": t[5][11],  # E6
        "7": t[3][11],  # E7
        "8": t[1][11]   # E8
    },
    "F":{
        "1": t[15][13], # F1
        "2": t[13][13], # F2
        "3": t[11][13], # F3
        "4": t[9][13],  # F4
        "5": t[7][13],  # F5
        "6": t[5][13],  # F6
        "7": t[3][13],  # F7
        "8": t[1][13]   # F8
    },
    "G":{
        "1": t[15][15], # G1
        "2": t[13][15], # G2
        "3": t[11][15], # G3
        "4": t[9][15],  # G4
        "5": t[7][15],  # G5
        "6": t[5][15],  # G6
        "7": t[3][15],  # G7
        "8": t[1][15]   # G8
    },
    "H":{
        "1": t[15][17], # H1
        "2": t[13][17], # H2
        "3": t[11][17], # H3
        "4": t[9][17],  # H4
        "5": t[7][17],  # H5
        "6": t[5][17],  # H6
        "7": t[3][17],  # H7
        "8": t[1][17]   # H8
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