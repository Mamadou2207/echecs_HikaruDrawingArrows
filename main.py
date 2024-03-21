import variables

echiquier = []     # Tableau représentant l'échiquier
fin_partie = False # Faux tant que la partie continue

def creer_echiquier(echiquier):
    """Crée un échiquier à l'aide d'un tableau à 2 dimensions

    Args:
        echiquier (list): Tableau à 2 dimensions
    """
    for loop in range(19):                             # Répéter 19 fois :
        ligne = []                                         # Tableau ligne dans echiquier
        for loop in range(19):                             # Répéter 19 fois :
                ligne.append(" ")                              # Nouvel indice ayant pour valeur " "
        echiquier.append(ligne)                            # Nouvel indice du tableau echiquier ayant pour valeur un tableau ligne
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
        echiquier[3][i*2+1] = variables.pion_n      # Dessine Pion Noir
        echiquier[13][i*2+1] = variables.pion_b     # Dessine Pion Blanc
    echiquier[15][3] = variables.tour_b         # Dessine Tour Blanche Gauche
    echiquier[15][17] = variables.tour_b        # Dessine Tour Blanche Droite
    echiquier[15][5] = variables.cavalier_b     # Dessine Cavalier Blanc Gauche
    echiquier[15][15] = variables.cavalier_b    # Dessine Cavalier Blanc Droite
    echiquier[15][7] = variables.fou_b          # Dessine Fou Blanc Gauche
    echiquier[15][13] = variables.fou_b         # Dessine Fou Blanc Droite
    echiquier[15][9] = variables.reine_b        # Dessine Reine Blanche
    echiquier[15][11] = variables.roi_b         # Dessine Roi Blanc
    echiquier[1][3] = variables.tour_n          # Dessine Tour Noir Gauche
    echiquier[1][17] = variables.tour_n         # Dessine Tour Noir Droite
    echiquier[1][5] = variables.cavalier_n      # Dessine Cavalier Noir Gauche
    echiquier[1][15] = variables.cavalier_n     # Dessine Cavalier Noir Droite
    echiquier[1][7] = variables.fou_n           # Dessine Fou Noir Gauche
    echiquier[1][13] = variables.fou_n          # Dessine Fou Noir Droite
    echiquier[1][9] = variables.roi_n           # Dessine Roi Noir
    echiquier[1][11] = variables.reine_n        # Dessine Reine Blanche

joueur1 = input("Nom Joueur 1 : ")    # Demande le nom du Joueur 1
joueur2 = input("Nom Joueur 2 : ")    # Demande le nom du Joueur 2
prochain_tour = joueur1               # Donne le tour au Joueur 1

def tour_joueur(joueur1, joueur2, prochain_tour):
    """Système de tour par tour

    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        prochain_tour (str): Nom du joueur ayant le droit de joueur
    """
    if prochain_tour == joueur1:          # Si le prochain tour est au joueur 1 :
        print(f"Tour de {prochain_tour}")     # Indique à qui est le tour
        prochain_tour = joueur2               # Donne le tour au joueur 2
    elif prochain_tour == joueur2:        # Si le prochain tour est au joueur 2 :
        print(f"Tour de {prochain_tour}")     # Indique à qui est le tour
        prochain_tour = joueur1               # Donne le tour au joueur 1
 
def forfait(joueur1, joueur2, prochain_tour):
    """Déclare forfait et réinitialise l'échiquier
    
    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        prochain_tour (str): Nom du joueur ayant le droit de joueur
    """
    if prochain_tour == joueur1:              # Si le Joueur 1 a déclaré forfait :
        print(f"{joueur1} a déclaré forfait")     # Indique qu'il déclare forfait
        creer_echiquier(echiquier)                # Réinitialise l'échiquier
    elif prochain_tour == joueur2:            # Si le Joueur 2 a déclaré forfait :
        print(f"{joueur2} a déclaré forfait")     # Indique qu'il déclare forfait
        creer_echiquier(echiquier)                # Réinitialise l'échiquier  
 
def match_nul(joueur1, joueur2, prochain_tour):
    """Propose un match nul au joueur adverse et gère sa réponse
    
    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        prochain_tour (str): Nom du joueur ayant le droit de joueur
    
    Returns:
        (bool): Vrai si la partie est nulle, sinon Faux
    """
    if prochain_tour == joueur1:                                                 # Si la fonction est appelée par le Joueur 1 :
        reponse = input(f"{joueur2}, acceptez-vous le match nul ? (Oui/Non) : ")    # Demande à l'adversaire s'il accepte :
        if reponse.lower() == "oui":                                                # Si oui :
            print("Match nul !")                                                        # Match Nul
            creer_echiquier(echiquier)                                                  # Réinitialise l'échiquier
            return True                                                                 # Indique que la partie est nulle
        else:                                                                    # Sinon :
            print("Le match nul est refusé. La partie continue.")                    # Match nul refusé
            return False                                                             # Indique que la partie reprend
    elif prochain_tour == joueur2:                                               # Si la fonction est appelée par le Joueur 2 :
        reponse = input(f"{joueur1}, acceptez-vous le match nul ? (Oui/Non) : ")    # Demande à l'adversaire s'il accepte :
        if reponse.lower() == "oui":                                                # Si oui :
            print("Match nul !")                                                        # Match Nul
            creer_echiquier(echiquier)                                                  # Réinitialise l'échiquier
            return True                                                                 # Indique que la partie est nulle
        else:                                                                    # Sinon :
            print("Le match nul est refusé. La partie continue.")                    # Match nul refusé
            return False                                                             # Indique que la partie reprend

def afficher_echiquier(echiquier):
    """Affiche l'échiquier

    Args:
        echiquier (list): Tableau à 2 dimensions
    """
    for x in range(19):                     # Répéter 19 fois :
        for y in range(19):                     # Répéter 19 fois :
            print(echiquier[x][y], end=" ")         # Imprimer tableau ligne du tableau echiquier
        print()                                 # Imprimer Saut de ligne
    tour_joueur()                           # Appel de la fonction tour_joueur
    return echiquier                        # Renvoyer échiquier

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
# print(dico_coords["D"]["1"])

def est_majuscule(caractere):
    """Vérifie si un caractère est majuscule ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): True or False
    """
    return 'A' <= caractere <= 'H' # Vérifie si l'encodage UTF-8 du caractère est entre A et H

def est_chiffre(caractere):
    """Vérifie si un caractère est chiffre ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): True of False
    """
    return '1' <= caractere <= '8' # Vérifie si l'encodage UTF-8 du caractère est entre 1 et 8
    
def reco_coordonnees(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): Indices x et y de l'échiquier
    
    Returns:
        (list): Dictionnaire à 2 dimensions 
    """
    x = coordonnees[0]       # Attribue le premier caractere de la chaine à la variable x
    y = coordonnees[1]       # Attribue le deuxième caractere de la chaine à la variable y
    est_majuscule(x)         # Vérifie si y est un nombre
    est_chiffre(y)           # Vérifie si y est un chiffre
    return dico_coords[x][y] # Renvoie les indices de l'échiquier correspondant aux coordonnées     

# TEST :
# print(reco_coordonnees(input("Coordonnées : ")))

""" NON OPERATIONNEL :
def deplacer(pos1, pos2):
    pos1 = reco_coordonnees(pos1)
    pos2 = reco_coordonnees(pos2)
    pos2 = pos1
    pos1 = " "
    return echiquier
"""

def deplacer(x1, y1, x2, y2, echiquier):
    """Déplace une pièce d'un point A à un point B

    Args:
        x1 (int): Coordonnée x du point A
        y1 (int): Coordonnée x du point B
        x2 (int): Coordonnée y du point A
        y2 (int): Coordonnée y du point B
        echiquier (list): Tableau à 2 dimensions
    """
    echiquier[x2][y2] = echiquier[x1][y1] # valeur point B devient valeur point A
    echiquier[x1][y1] = " "               # valeur point A devient "nulle"
    
def verif(axe, point):
    """Vérifie que le point existe

    Args:
        axe (list): Représente toute les valeurs possible à l'axe
        point (int): Une des deux oordonnées du point B

    Returns:
        (bool): Vrai si y2 est possible sinon Faux
    """
    for v in axe :      # Pour chaque valeur présente dans ligne :
        if point == v :     # Si x2 est présent dans ligne :
            return True     # Renvoyer Vrai
    return False        # Sinon renvoyer Faux

def condition_tour_verticale(x2, y1, y2):
    """Conditionne le déplacement à la verticale

    Args:
        x2 (int): Coordonnée x du point B
        y1 (int): Coordonnée y du point A
        y2 (int): Coordonnée y du point B

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    if y2 == y1 and verif(variables.colonne, x2) == True: # Si la tour peut effectuer ce déplacement :
        return True                                           # Renvoyer Vrai
    else:                                                 # Sinon :
        return False                                          # Renvoyer Faux


def condition_tour_horizontale(y2, x1, x2):
    """Conditionne le déplacement à l'horizontal

    Args:
        y2 (int): Coordonnée y du point B
        x1 (int): Coordonnée x du point A
        x2 (int): Coordonnée x du point B

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    if x2 == x1 and verif(variables.ligne, y2) == True: # Si la tour peut effectuer ce déplacement :
        return True                                         # Renvoyer Vrai
    else:                                               # Sinon :
        return False                                        # Renvoyer Faux

def deplacement(piece, x1, y1, x2, y2, echiquier):
    """Autorise les pièces à se déplacer si elles respectent les conditions requises

    Args:
        piece (str): Nom et couleur de la pièce
        x1 (int): Coordonnée x du point A
        y1 (int): Coordonnée y du point A
        x2 (int): Coordonnée x du point B
        y2 (int): Coordonnée y du point B
        echiquier (list): Tableau à 2 dimensions
    """
    if piece == variables.pion_b:                                                                      # Si la pièce déplacé est un Pion Blanc :
        if x2 == x1-2 and y2 == y1:                                                                        # Si le Pion peut effectuer ce déplacement :
            deplacer(x1,y1,x2,y2,echiquier)                                                                    # Déplace la pièce du point A au point B
            # Non terminé (il manque le +2 quand il n'a pas bougé, le fait de manger une pièce en diagonale et le "en passant")
        else:                                                                                          # Sinon :
            print("Tu ne peut pas déplacer le Pion Blanc ici")                                             # Afficher message d'erreur
    elif piece == variables.pion_n:                                                                    # Si la pièce déplacé est un Pion Noir :
        if x2 == x1+2 and y2 == y1:                                                                        # Si le Pion peut effectuer ce déplacement :
            deplacer(x1,y1,x2,y2,echiquier)                                                                    # Déplace la pièce du point A au point B
            # Non terminé (il manque le +2 quand il n'a pas bougé, le fait de manger une pièce en diagonale et le "en passant")
        else:                                                                                          # Sinon :
            print("Tu ne peut pas déplacer le Pion Noir ici")                                              # Afficher message d'erreur
    elif piece == variables.tour_b:                                                                    # Si la pièce déplacé est une Tour Blanche :
        if condition_tour_verticale(x2,y1,y2) == True or condition_tour_horizontale(y2,x1,x2) == True:     # Si la Tour peut effectuer ce déplacement :
            deplacer(x1,y1,x2,y2,echiquier)                                                                    # Déplace la pièce du point A au point B
        else:                                                                                          # Sinon :
            print("Tu ne peux pas déplacer la Tour Blanche ici")                                           # Afficher message d'erreur
    elif piece == variables.tour_n:                                                                    # Si la pièce déplacé est une Tour Noire :
        if condition_tour_verticale(x2,y1,y2) == True or condition_tour_horizontale(y2,x1,x2) == True:     # Si la Tour peut effectuer ce déplacement :
            deplacer(x1,y1,x2,y2,echiquier)                                                                    # Déplace la pièce du point A au point B
        else:                                                                                          # Sinon :
            print("Tu ne peux pas déplacer la Tour Noire ici")                                             # Afficher message d'erreur
    # TEMPORAIRE :
    elif piece == variables.cavalier_b:
        deplacer(x1,y1,x2,y2,echiquier) 
    elif piece == variables.cavalier_n:
        deplacer(x1,y1,x2,y2,echiquier) 
    elif piece == variables.fou_b:
        deplacer(x1,y1,x2,y2,echiquier)
    elif piece == variables.fou_n:
        deplacer(x1,y1,x2,y2,echiquier)
    elif piece == variables.reine_b:
        deplacer(x1,y1,x2,y2,echiquier)
    elif piece == variables.reine_n:
        deplacer(x1,y1,x2,y2,echiquier)
    elif piece == variables.roi_b:
        deplacer(x1,y1,x2,y2,echiquier)
    elif piece == variables.reine_b:
        deplacer(x1,y1,x2,y2,echiquier) 

# TEST :
#deplacement(variables.pion_b, 13, 3, 11, 3, echiquier)
#deplacement(variables.pion_b, 13, 3, 9, 3, echiquier)
#deplacement(variables.tour_b, 1, 17, 7, 3, echiquier)
#deplacement(variables.tour_b, 1, 17, 7, 17, echiquier)
#deplacement(variables.tour_b, 1, 3, 1, 17, echiquier)
#afficher_echiquier(echiquier)