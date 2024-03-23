import variables
import dictionnaires

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
            elif x%2 == 0 and echiquier[x][y] == " ":          # Si le reste de x par 2 != à 0 et que la valeur = " " :
                echiquier[x][y] = "-"                              # Dessine quadrillage horizontal
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

joueur1 = input("Nom Joueur 1 : ") # Demande le nom du Joueur 1
joueur2 = input("Nom Joueur 2 : ") # Demande le nom du Joueur 2
prochain_tour = joueur1            # Donne le tour au Joueur 1

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
    for x in range(19):                          # Répéter 19 fois :
        for y in range(19):                          # Répéter 19 fois :
            print(echiquier[x][y], end=" ")              # Imprimer tableau ligne du tableau echiquier
        print()                                      # Imprimer Saut de ligne
    tour_joueur(joueur1, joueur2, prochain_tour) # Appel de la fonction tour_joueur
    return echiquier                             # Renvoyer échiquier

# TEST :
creer_echiquier(echiquier)    # Crée un échiquier avec les pièces à leur positions par défaut
afficher_echiquier(echiquier) # Affiche l'échiquier sur la console python

def est_majuscule(caractere):
    """Vérifie si un caractère est majuscule ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): True or False
    """
    caractere.upper()
    if 'A' <= caractere <= 'H': # Si l'encodage UTF-8 du caractère est entre A et H
        return caractere            # Renvoyer caractère 
    return False
def est_chiffre(caractere):
    """Vérifie si un caractère est chiffre ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): True of False
    """
    if '1' <= caractere <= '8': # Si l'encodage UTF-8 du caractère est entre 1 et 8
        return caractere            # Renvoyer caractère
    return False
    
def reco_coordonnees(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): Indices x et y de l'échiquier
    
    Returns:
        (list): Dictionnaire à 2 dimensions 
    """
    x = coordonnees[0]                        # Attribue le premier caractere de la chaine à la variable x
    y = coordonnees[1]                        # Attribue le deuxième caractere de la chaine à la variable y
    est_majuscule(x)                          # Vérifie si x est un nombre
    est_chiffre(y)                            # Vérifie si y est un chiffre
    return dictionnaires.coords.get(x).get(y) # Renvoie les indices de l'échiquier correspondant aux coordonnées

def reco_coordonnees_x(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): Indice x de l'échiquier
    
    Returns:
        (list): Dictionnaire à 2 dimensions 
    """
    x = coordonnees[0]                        # Attribue le premier caractere de la chaine à la variable x
    y = coordonnees[1]                        # Attribue le deuxième caractere de la chaine à la variable y
    est_majuscule(x)                          # Vérifie si x est un nombre
    est_chiffre(y)                            # Vérifie si y est un chiffre
    return dictionnaires.coords.get(x).get(y).get("x") # Renvoie les indices de l'échiquier correspondant aux coordonnées

def reco_coordonnees_y(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): Indice y de l'échiquier
    
    Returns:
        (list): Dictionnaire à 2 dimensions 
    """
    x = coordonnees[0]                        # Attribue le premier caractere de la chaine à la variable x
    y = coordonnees[1]                        # Attribue le deuxième caractere de la chaine à la variable y
    est_majuscule(x)                          # Vérifie si x est un nombre
    est_chiffre(y)                            # Vérifie si y est un chiffre
    return dictionnaires.coords.get(x).get(y).get("y") # Renvoie les indices de l'échiquier correspondant aux coordonnées
# TEST :
# print(reco_coordonnees("D8"))

def deplacer(pos1, pos2, echiquier):
    """Déplace une pièce d'un point A à un point B sur l'échiquier

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (list): Renvoie le déplacement de la pièce sur l'échiquier
    """
    pos1 = reco_coordonnees(pos1)                                                     # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                                                     # Récupère les indices de l'échiquier correspondant au point B
    echiquier[pos2.get("x")][pos2.get("y")] = echiquier[pos1.get("x")][pos1.get("y")] # Valeur du point B devient celle du point A
    echiquier[pos1.get("x")][pos1.get("y")] = " "                                     # Supprime la pièce du Point A
    return echiquier                                                                  # Renvoie l'échiquier après le déplacement de la pièce
    
# TEST :
# deplacer(input("Point A : "), input("Point B : "), echiquier)
# afficher_echiquier(echiquier)
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

    

def condition_tour_verticale(pos1, pos2):
    """Conditionne le déplacement à la verticale

    Args:
        x2 (int): Coordonnée x du point B
        y1 (int): Coordonnée y du point A
        y2 (int): Coordonnée y du point B

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    if reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) and verif(variables.colonne,reco_coordonnees_x(pos2)) == True: # Si la tour peut effectuer ce déplacement :
        return True                                         # Renvoyer Vrai
    else:                                               # Sinon :
        return False                                        # Renvoyer Faux

def condition_tour_horizontale(pos1, pos2):
    """Conditionne le déplacement à l'horizontal

    Args:
        y2 (int): Coordonnée y du point B
        x1 (int): Coordonnée x du point A
        x2 (int): Coordonnée x du point B

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    if reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) and  verif(variables.ligne,reco_coordonnees_y(pos2)) == True: # Si la tour peut effectuer ce déplacement :
        return True                                         # Renvoyer Vrai
    else:                                               # Sinon :
        return False                                        # Renvoyer Faux

def condtion_fou_diagonale(pos1, pos2):
    """Conditionne le déplacement en diagonale

    Args:
        pos1 (str): la position initiale
        pos2 (str): la position finale

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    if abs(reco_coordonnees_x(pos2) - reco_coordonnees_x(pos1)) != abs(reco_coordonnees_y(pos2) - reco_coordonnees_y(pos1)):  # Si le fou peut effectuer ce déplacement
        return False                                                                                        # Renvoyer Faux
    return True                                                                                           # Sinon Vrai

def condition_cavalier(pos1, pos2):
    """Conditionne le déplacement en L du cavalier

    Args:
        pos1 (str): la position initiale
        pos2 (str): la position finale

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    if (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) + 4 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) + 2) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) + 4 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) - 2) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) + 2 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) + 4) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) - 2 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) + 4) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) - 4 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) + 2) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) - 4 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) - 2) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) + 2 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) - 4) or (reco_coordonnees_x(pos2) == reco_coordonnees_x(pos1) - 2 and reco_coordonnees_y(pos2) == reco_coordonnees_y(pos1) + 4):        # Si le fou peut effectuer ce déplacement
        return True                 # Renvoyer Faux
    return False                   # Sinon Vrai

def deplacement(piece, pos1, pos2, echiquier):
    """Autorise les pièces à se déplacer si elles respectent les conditions requises

    Args:
        piece (str): Nom et couleur de la pièce
        pos1 (int): Point A
        pos2 (int): Point B
        echiquier (list): Tableau à 2 dimensions
    """
    a = reco_coordonnees(pos1)                                                                                                                                                 # Récupère les indices de l'échiquier correspondant au point A
    b = reco_coordonnees(pos2)                                                                                                                                                 # Récupère les indices de l'échiquier correspondant au point B
    if piece == variables.pion_b:                                                                                                                                              # Si la pièce déplacé est un Pion Blanc :
        if echiquier[b.get("x")+2][b.get("y")] == echiquier[a.get("x")][a.get("y")]:                                                                                               # Si x2 = x1 et y2 - 1 = y1 :
            deplacer(pos1, pos2, echiquier)                                                                                                                                            # Autoriser le déplacement
        elif echiquier[b.get("x")+4][b.get("y")] == echiquier[13][a.get("y")]:                                                                                                     # Si x2 = x1 et y2 - 2 = y1 :
            deplacer(pos1, pos2, echiquier)                                                                                                                                            # Autoriser le déplacement
        elif echiquier[b.get("x")+2][b.get("y")-2] or echiquier[b.get("x")+2][b.get("y")+2] == echiquier[a.get("x")][a.get("y")] and echiquier[b.get("x")][b.get("y")] != " ":     # Si x2 - 1 = x1 et y2 - 1 = y1 OU x2 + 1 = x1 et y2 - 1 = y1 ET que le point B n'est pas vide :
            deplacer(pos1, pos2, echiquier)                                                                                                                                            # Autoriser le déplacement
            # Non terminé (il manque, le "en passant")
        else:                                                                                                                                                                      # Sinon :
            print("Tu ne peux pas déplacer le Pion Blanc ici")                                                                                                                         # Afficher message d'erreur    # Afficher message d'erreur
    if piece == variables.pion_n:                                                                                                                                              # Si la pièce déplacé est un Pion Blanc :
        if echiquier[b.get("x")-2][b.get("y")] == echiquier[a.get("x")][a.get("y")]:                                                                                               # Si x2 = x1 et y2 - 1 = y1 :
            deplacer(pos1, pos2, echiquier)                                                                                                                                            # Autoriser le déplacement
        elif echiquier[b.get("x")-4][b.get("y")] == echiquier[3][a.get("y")]:                                                                                                     # Si x2 = x1 et y2 - 2 = y1 :
            deplacer(pos1, pos2, echiquier)                                                                                                                                            # Autoriser le déplacement
        elif echiquier[b.get("x")-2][b.get("y")+2] or echiquier[b.get("x")-2][b.get("y")-2] == echiquier[a.get("x")][a.get("y")] and echiquier[b.get("x")][b.get("y")] != " ":     # Si x2 - 1 = x1 et y2 - 1 = y1 OU x2 + 1 = x1 et y2 - 1 = y1 ET que le point B n'est pas vide :
            deplacer(pos1, pos2, echiquier)                                                                                                                                            # Autoriser le déplacement
            # Non terminé (il manque, le "en passant")
        else:                                                                                                                                                                      # Sinon :
            print("Tu ne peux pas déplacer le Pion Blanc ici")                                                                                                                         # Afficher message d'erreur    # Afficher message d'erreur
    if piece == variables.tour_b:
        if condition_tour_verticale(pos1, pos2) == True or condition_tour_horizontale(pos1, pos2) == True:  #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                    #Alors Déplace la pièce du point A au point B
        else :                                                                                              #Sinon :
            print("Tu ne peux pas déplacer le Tour Blanche ici")                                               # Afficher message d'erreur
    if piece == variables.tour_n:
        if condition_tour_verticale(pos1, pos2) == True or condition_tour_horizontale(pos1, pos2) == True:  #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                     #Alors Déplace la pièce du point A au point B
        else : 
            print("Tu ne peux pas déplacer le Tour Noir ici")
    if piece == variables.fou_b :                                                                           
        if condtion_fou_diagonale(pos1, pos2) :                                                             #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                     #Alors Déplace la pièce du point A au point B
        else :                                                                                              #Sinon :
            print("Tu ne peux pas déplacer le Fou Blanc ici")                                                   # Afficher message d'erreur
    if piece == variables.fou_n :
        if condtion_fou_diagonale(pos1, pos2) :                                                             #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                     #Alors Déplace la pièce du point A au point B
        else :                                                                                              #Sinon :
            print("Tu ne peux pas déplacer le Fou Noir ici")                                                    # Afficher message d'erreur
    if piece == variables.reine_b:
        if condtion_fou_diagonale(pos1, pos2) or condtion_fou_diagonale(pos1, pos2) or condtion_fou_diagonale(pos1, pos2) :     #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                                         #Alors Déplace la pièce du point A au point B
        else :                                                                                                                  #Sinon :
            print("Tu ne peux pas déplacer la Reine Blanche ici")                                                                   # Afficher message d'erreur    
    if piece == variables.reine_n:
        if condtion_fou_diagonale(pos1, pos2) or condtion_fou_diagonale(pos1, pos2) or condtion_fou_diagonale(pos1, pos2) :     #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                                         #Alors Déplace la pièce du point A au point B
        else :                                                                                                                   #Sinon :
            print("Tu ne peux pas déplacer la Reine Noir ici")                                                                      # Afficher message d'erreur
    elif piece == variables.cavalier_b:
        if condition_cavalier(pos1, pos2) :                                                                                     #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                                         #Alors Déplace la pièce du point A au point B
        else :                                                                                                                   #Sinon :
            print("Tu ne peux pas déplacer le Cavalier Blanc ici")                                                                  # Afficher message d'erreur
    elif piece == variables.cavalier_n:
        if condition_cavalier(pos1, pos2) :                                                                                     #Si les conditions sont vrai
            deplacer(pos1, pos2, echiquier)                                                                                         #Alors Déplace la pièce du point A au point B
        else :                                                                                                                   #Sinon :
            print("Tu ne peux pas déplacer le Cavalier Noir ici")                                                                   # Afficher message d'erreur  
# TEST :
deplacement(variables.cavalier_b, "B1", "A3", echiquier)
afficher_echiquier(echiquier)


"""
    # TEMPORAIRE :
    elif piece == variables.cavalier_b:
        deplacer(A, B, echiquier)
    elif piece == variables.cavalier_n:
        deplacer(A, B, echiquier) 
    elif piece == variables.fou_b:
        deplacer(A, B, echiquier)
    elif piece == variables.fou_n:
        deplacer(A, B, echiquier)
    elif piece == variables.reine_b:
        deplacer(A, B, echiquier)
    elif piece == variables.reine_n:
        deplacer(A, B, echiquier)
    elif piece == variables.roi_b:
        deplacer(A, B, echiquier)
    elif piece == variables.reine_b:
        deplacer(A, B, echiquier)
        """
