import variables
import dictionnaires

def creer_echiquier(echiquier):
    """Crée un échiquier à l'aide d'un tableau à 2 dimensions

    Args:
        echiquier (list): Tableau à 2 dimensions
    """
    for loop in range(19):                            # Répéter 19 fois :
        ligne = []                                        # Tableau ligne dans echiquier
        for loop in range(19):                            # Répéter 19 fois :
                ligne.append(" ")                             # Nouvel indice ayant pour valeur " "
        echiquier.append(ligne)                           # Nouvel indice du tableau echiquier ayant pour valeur un tableau ligne
    for x in range(19):                               # Répéter 19 fois :
        for y in range(19):                               # Répéter 19 fois :
            if y%2 == 0:                                      # Si le reste de y par 2 != à 0 :
                echiquier[x][y] = "|"                             # Dessine quadrillage vertical
                y *= 3                                            # Décalage permettant le quadrillage (Multiplier par 3 à chaque boucle)
            elif x%2 == 0 and echiquier[x][y] == " ":         # Si le reste de x par 2 != à 0 et que la valeur = " " :
                echiquier[x][y] = "-"                             # Dessine quadrillage horizontal
    for i in range(8):                                # Répéter 8 fois :
        i += 1                                            # Ajouter 1 à chaque boucle
        echiquier[i*2-1][1] = 9-i                         # Affiche les coordonnées y (axe des ordonnées) 
        echiquier[17][i*2+1] = chr(ord("A")+i-1)          # Affiche les coordonnées x (axe des abscisses) 
        echiquier[3][i*2+1] = variables.pion_n            # Dessine Pion Noir
        echiquier[13][i*2+1] = variables.pion_b           # Dessine Pion Blanc
    echiquier[15][3] = variables.tour_b               # Dessine Tour Blanche Gauche
    echiquier[15][17] = variables.tour_b              # Dessine Tour Blanche Droite
    echiquier[15][5] = variables.cavalier_b           # Dessine Cavalier Blanc Gauche
    echiquier[15][15] = variables.cavalier_b          # Dessine Cavalier Blanc Droite
    echiquier[15][7] = variables.fou_b                # Dessine Fou Blanc Gauche
    echiquier[15][13] = variables.fou_b               # Dessine Fou Blanc Droite
    echiquier[15][9] = variables.reine_b              # Dessine Reine Blanche
    echiquier[15][11] = variables.roi_b               # Dessine Roi Blanc
    echiquier[1][3] = variables.tour_n                # Dessine Tour Noir Gauche
    echiquier[1][17] = variables.tour_n               # Dessine Tour Noir Droite
    echiquier[1][5] = variables.cavalier_n            # Dessine Cavalier Noir Gauche
    echiquier[1][15] = variables.cavalier_n           # Dessine Cavalier Noir Droite
    echiquier[1][7] = variables.fou_n                 # Dessine Fou Noir Gauche
    echiquier[1][13] = variables.fou_n                # Dessine Fou Noir Droite
    echiquier[1][9] = variables.reine_n               # Dessine Reine Noir
    echiquier[1][11] = variables.roi_n                # Dessine Roi Blanche

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
        return prochain_tour                  # Renvoie la variable
    elif prochain_tour == joueur2:        # Si le prochain tour est au joueur 2 :
        print(f"Tour de {prochain_tour}")     # Indique à qui est le tour
        prochain_tour = joueur1               # Donne le tour au joueur 1
        return prochain_tour                  # Renvoie la variable
 
def forfait(joueur1, joueur2, prochain_tour, echiquier):
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
 
def match_nul(joueur1, joueur2, prochain_tour, echiquier):
    """Propose un match nul au joueur adverse et gère sa réponse
    
    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        prochain_tour (str): Nom du joueur ayant le droit de jouer
    
    Returns:
        (bool): Vrai ou Faux
    """
    if prochain_tour == joueur1:                                                 # Si la fonction est appelée par le Joueur 1 :
        reponse = input(f"{joueur2}, acceptez-vous le match nul ? (Oui/Non) : ")     # Demande à l'adversaire s'il accepte
        if reponse.lower() == "oui":                                                 # Si oui :
            print("Match nul !")                                                         # Match Nul
            creer_echiquier(echiquier)                                                   # Réinitialise l'échiquier
            return True                                                                  # Indique que la partie est nulle
        else:                                                                        # Sinon :
            print("Le match nul est refusé. La partie continue.")                        # Match nul refusé
            return False                                                                 # Indique que la partie reprend
    elif prochain_tour == joueur2:                                               # Si la fonction est appelée par le Joueur 2 :
        reponse = input(f"{joueur1}, acceptez-vous le match nul ? (Oui/Non) : ")     # Demande à l'adversaire s'il accepte
        if reponse.lower() == "oui":                                                 # Si oui :
            print("Match nul !")                                                         # Match Nul
            creer_echiquier(echiquier)                                                   # Réinitialise l'échiquier
            return True                                                                  # Indique que la partie est nulle
        else:                                                                        # Sinon :
            print("Le match nul est refusé. La partie continue.")                        # Match nul refusé
            return False                                                                 # Indique que la partie reprend

def afficher_echiquier(echiquier):
    """Affiche l'échiquier

    Args:
        echiquier (list): Tableau à 2 dimensions
    """
    for x in range(19):                     # Répéter 19 fois :
        for y in range(19):                     # Répéter 19 fois :
            print(echiquier[x][y], end=" ")         # Imprimer tableau ligne du tableau echiquier
        print()                                 # Imprimer Saut de ligne
    return echiquier                        # Renvoyer échiquier

def est_majuscule(caractere):
    """Vérifie si un caractère est majuscule ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): Vrai ou Faux
    """
    caractere.upper()
    if 'A' <= caractere <= 'H': # Si l'encodage UTF-8 du caractère est entre A et H :
        return True                 # Renvoyer Vrai
    return False                # Sinon Faux

def est_chiffre(caractere):
    """Vérifie si un caractère est chiffre ou non

    Args:
        caractere (str): UTF-8

    Returns:
        (bool): Vrai ou Faux
    """
    if '1' <= caractere <= '8': # Si l'encodage UTF-8 du caractère est entre 1 et 8 :
        return True                 # Renvoyer caractère
    return False                # Renvoyer Faux

def verif(list, point):
    """Vérifie que le point existe

    Args:
        list (list): Représente toute les valeurs possible à l'axe
        point (int): Une des deux oordonnées du point B

    Returns:
        (bool): Vrai ou Faux
    """
    for v in list :     # Pour chaque valeur présente dans liste :
        if point == v :     # Si va est présent dans la liste :
            return True         # Renvoyer Vrai
    return False        # Sinon renvoyer Faux

def reco_coordonnees(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): Indices x et y de l'échiquier
    
    Returns:
        (list): Dictionnaire à 2 dimensions 
    """
    x = coordonnees[0]                                # Récupère le premier caractere de la chaine
    y = coordonnees[1]                                # Récupère le deuxième caractere de la chaine
    if est_majuscule(x) == True:                      # Vérifie si x est une lettre majuscule compris entre A et H :
        if est_chiffre(y) == True:                        # Vérifie si y est un chiffre compris entre 1 et 8 :
            return dictionnaires.coords.get(x).get(y)         # Renvoie les indices de l'échiquier correspondant aux coordonnées
    return False                                      # Renvoyer Faux

def reco_allies(pos1, pos2, echiquier):
    """Détecte si la pièce au point B est une pièce allié

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                    # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                    # Récupère les indices de l'échiquier correspondant au point B
    pos1 = echiquier[pos1.get("x")][pos1.get("y")]   # Récupère la valeur du point A
    pos2 = echiquier[pos2.get("x")][pos2.get("y")]   # Récupère la valeur du point B
    if pos1 != " ":                                  # Si la valeur du point B n'est pas vide :
        if verif(variables.blanc, pos2) == True:         # Si la pièce au point B est blanche :
            if verif(variables.blanc, pos1) == True:         # Si la pièce au point A est blanche :
                return True                                      # Renvoyer Vrai
        elif verif(variables.noir, pos2) == True:          # Si la pièce au point B est noire :
            if verif(variables.noir, pos1) == True:          # Si la pièce au point A est noire :
                return True                                      # Renvoyer Vrai
    return False                                     # Sinon renvoyer Faux

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
    echiquier[pos2.get("x")][pos2.get("y")] = echiquier[pos1.get("x")][pos1.get("y")] # La valeur du point B devient celle du point A
    echiquier[pos1.get("x")][pos1.get("y")] = " "                                     # Remplace la valeur du point A par " "
    return echiquier                                                                  # Renvoie l'échiquier après le déplacement de la pièce

def condition_pion(pos1, pos2, echiquier):
    """Conditionne le déplacement du pion

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions
        
    Returns: 
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                                                                    # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                                                                    # Récupère les indices de l'échiquier correspondant au point B
    piece = echiquier[pos1.get("x")][pos1.get("y")]                                                  # Récupère la pièce se trouvant au point A
    if piece == variables.pion_b:                                                                    # Si le pion est blanc :
        if echiquier[pos2.get("x")+2][pos2.get("y")] == echiquier[pos1.get("x")][pos1.get("y")]:         # Si x2 + 2 = x1 et y2 = y1 :
            return True                                                                                      # Renvoyer Vrai
        elif echiquier[pos2.get("x")+4][pos2.get("y")] == echiquier[13][pos1.get("y")]:                  # Si x2 + 4 = 13 et y2 = y1 :
            return True                                                                                      # Renovyer Vrai
        elif echiquier[pos2.get("x")+2][pos2.get("y")-2] == echiquier[pos1.get("x")][pos1.get("y")]:     # Si x2 + 2 = x1 et y2 - 2 = y1 :
            if echiquier[pos2.get("x")][pos2.get("y")] != " ":                                               # Si le point B est différent de " " :
                return True                                                                                      # Renvoyer Vrai
        elif echiquier[pos2.get("x")+2][pos2.get("y")+2] == echiquier[pos1.get("x")][pos1.get("y")]:     # Si x2 + 2 = x1 et y2 + 2 = y1 :
            if echiquier[pos2.get("x")][pos2.get("y")] != " ":                                               # Si le point B est différent de " " :
                return True                                                                                      # Renvoyer Vrai
    elif piece == variables.pion_n:                                                                  # Si le pion est noir :
        if echiquier[pos2.get("x")-2][pos2.get("y")] == echiquier[pos1.get("x")][pos1.get("y")]:         # Si x2 - 2 = x1 et y2 = y1 :
            return True                                                                                      # Renvoyer Vrai
        elif echiquier[pos2.get("x")-4][pos2.get("y")] == echiquier[3][pos1.get("y")]:                   # Si x2 - 4 = 3 et y2 = y1 :
            return True                                                                                      # Renvoyer Vrai
        elif echiquier[pos2.get("x")-2][pos2.get("y")-2] == echiquier[pos1.get("x")][pos1.get("y")]:     # Si x2 - 2 = x1 et y2 - 2 = y1 :
            if echiquier[pos2.get("x")][pos2.get("y")] != " ":                                               # Si le point B est différent de " " :
                return True                                                                                      # Renvoyer Vrai
        elif echiquier[pos2.get("x")-2][pos2.get("y")+2] == echiquier[pos1.get("x")][pos1.get("y")]:     # Si x2 - 2 = x1 et y2 + 2 = y1 :
            if echiquier[pos2.get("x")][pos2.get("y")] != " ":                                               # Si le point B est différent de " " :
                return True                                                                                      # Renvoyer Vrai
    return False                                                                                         # Renvoyer Faux

def condition_tour_verticale(pos1, pos2):
    """Conditionne le déplacement de la tour en vertical

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        
    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                           # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                           # Récupère les indices de l'échiquier correspondant au point B
    if pos2.get("y") == pos1.get("y"):                      # Si y2 = y1 :
        if verif(variables.colonne, pos2.get("x")) == True:     # Si x2 se situe dans les x utilisables :
            return True                                             # Renvoyer Vrai
    return False                                            # Sinon renvoyer Faux

def condition_tour_horizontale(pos1, pos2):
    """Conditionne le déplacement de la tour en horizontal

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B

    Returns:
        (bool): Vrai si les conditions sont respectées sinon Faux
    """
    pos1 = reco_coordonnees(pos1)                         # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                         # Récupère les indices de l'échiquier correspondant au point B
    if pos2.get("x") == pos1.get("x"):                    # Si x2 = x1 :
        if verif(variables.ligne, pos2.get("y")) == True:     # Si y2 se situe dans les y utlisables :
            return True                                           # Renvoyer Vrai
    return False                                          # Sinon renvoyer Faux

def condition_fou_diagonale(pos1, pos2):
    """Conditionne le déplacement du fou

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B

    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)          # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)          # Récupère les indices de l'échiquier correspondant au point B
    x = abs(pos2.get("x") - pos1.get("x")) # Valeur absolue de x2 - x1
    y = abs(pos2.get("y") - pos1.get("y")) # Valeur absolue de y2 - y1
    if x != y:                             # Si x est différent de y :
        return False                           # Renvoyer Faux
    return True                            # Sinon Vrai

def condition_cavalier(pos1, pos2):
    """Conditionne le déplacement du cavalier

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B

    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                # Récupère les indices de l'échiquier correspondant au point B
    if pos2.get("x") == pos1.get("x") + 4:       # Si x2 = x1 + 4 :
        if pos2.get("y") == pos1.get("y") + 2:       # Si y2 = y1 + 2 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 2:     # Si y2 = y1 - 2 :
            return True                                  # Renvoyer Vrai
    elif pos2.get("x") == pos1.get("x") + 2:     # Si x2 = x1 + 2 :
        if pos2.get("y") == pos1.get("y") + 4:       # Si y2 = y1 + 4 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 4:     # Si y2 = y1 - 4 :
            return True                                  # Renvoyer Vrai
    elif pos2.get("x") == pos1.get("x") - 2:     # Si x2 = x1 - 2 :
        if pos2.get("y") == pos1.get("y") + 4:       # Si y2 = y1 + 4 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 4:     # Si y2 = y1 - 4 :
            return True                                  # Renvoyer Vrai
    elif pos2.get("x") == pos1.get("x") - 4:     # Si x2 = x1 - 4 :
        if pos2.get("y") == pos1.get("y") + 2:       # Si y2 = y1 + 2 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 2:     # Si y2 = y1 - 2 :
            return True                                  # Renvoyer Vrai
    return False                                 # Sinon renvoyer Faux

def condition_roi(pos1, pos2):
    """Conditionne le déplacement du Roi

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B

    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                # Récupère les indices de l'échiquier correspondant au point B
    if pos2.get("x") == pos1.get("x") + 2:       # Si x2 = x1 + 2 :
        if pos2.get("y") == pos1.get("y"):           # Si y2 = y1 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") + 2:     # Si y2 = y1 + 2 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 2:     # Si y2 = y1 - 2 :
            return True                                  # Renvoyer Vrai
    elif pos2.get("x") == pos1.get("x") - 2:     # Si x2 = x1 - 2 :
        if pos2.get("y") == pos1.get("y"):           # Si y2 = y1 :
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") + 2:     # Si y2 = y1 + 2
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 2:     # Si y2 = y1 - 2
            return True                                  # Renvoyer Vrai
    elif pos2.get("x") == pos1.get("x"):         # Si x2 = x1
        if pos2.get("y") == pos1.get("y") + 2:       # Si y2 = y1 + 2:
            return True                                  # Renvoyer Vrai
        elif pos2.get("y") == pos1.get("y") - 2:     # Si y2 = y1 - 2
            return True                                  # Renvoyer Vrai
    return False                                 # Sinon renvoyer Faux

def deplacement(pos1, pos2, echiquier):
    """Autorise les pièces à se déplacer si elles respectent les conditions requises

    Args:
        pos1 (int): Coordonnées du point A
        pos2 (int): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions
    """
    piece = reco_coordonnees(pos1)                                     # Récupère les indices de l'échiquier correspondant au point A
    piece = echiquier[piece.get("x")][piece.get("y")]                  # Récupère la valeur du point A
    if reco_allies(pos1, pos2, echiquier) == False:                    # Si les pièces au point A et au point B ne dans le même camp :
        if piece == variables.pion_b:                                      # Si la pièce déplacée est un Pion Blanc :
            if condition_pion(pos1, pos2, echiquier) == True:                  # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
                # Non terminé (il manque, le "en passant")
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Pion Blanc ici")                 # Afficher message d'erreur
        if piece == variables.pion_n:                                      # Si la pièce déplacée est un Pion Noir :
            if condition_pion(pos1, pos2, echiquier) == True:                  # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Autoriser le déplacement
                # Non terminé (il manque, le "en passant")
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Pion Noir ici")                  # Afficher message d'erreur
        if piece == variables.tour_b:                                      # Si la pièce déplacée est un Tour Blanc :
            if condition_tour_verticale(pos1, pos2) == True:                   # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            elif condition_tour_horizontale(pos1, pos2) == True:               # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Tour Blanche ici")               # Afficher message d'erreur
        if piece == variables.tour_n:                                      # Si la pièce déplacée est un Tour Noir :
            if condition_tour_verticale(pos1, pos2) == True:                   # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            elif condition_tour_horizontale(pos1, pos2) == True:               # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Tour Noir ici")                  # Afficher message d'erreur
        if piece == variables.fou_b:                                       # Si la pièce déplacée est un Fou Blanc :
            if condition_fou_diagonale(pos1, pos2) == False:                   # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Fou Blanc ici")                  # Afficher message d'erreur
        if piece == variables.fou_n:                                       # Si la pièce déplacée est un Fou Noir :
            if condition_fou_diagonale(pos1, pos2) == False:                   # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Fou Noir ici")                   # Afficher message d'erreur
        if piece == variables.reine_b:                                     # Si la pièce déplacée est un Reine Blanc :
            if condition_fou_diagonale(pos1, pos2) == False:                   # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            elif condition_tour_verticale(pos1, pos2) == True:                 # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            elif condition_tour_horizontale(pos1, pos2) == True:               # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer la Reine Blanche ici")              # Afficher message d'erreur    
        if piece == variables.reine_n:                                     # Si la pièce déplacée est un Reine Noir :
            if condition_fou_diagonale(pos1, pos2) == False:                   # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            elif condition_tour_verticale(pos1, pos2) == True:                 # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            elif condition_tour_horizontale(pos1, pos2) == True:               # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer la Reine Noire ici")                # Afficher message d'erreur    
        elif piece == variables.cavalier_b:                                # Si la pièce déplacée est un Cavalier Blanc :
            if condition_cavalier(pos1, pos2) == True:                         # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Cavalier Blanc ici")             # Afficher message d'erreur
        elif piece == variables.cavalier_n:                                # Si la pièce déplacée est un Cavalier Noir :
            if condition_cavalier(pos1, pos2) == True:                         # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Cavalier Noir ici")              # Afficher message d'erreur
        elif piece == variables.roi_b:                                     # Si la pièce déplacée est un Roi Blanc :
            if condition_roi(pos1, pos2) == True:                              # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Roi Blanc ici")                  # Afficher message d'erreur
        elif piece == variables.roi_n:                                     # Si la pièce déplacée est un Roi Noir :
            if condition_roi(pos1, pos2) == True:                              # Si les conditions sont vérifiées :
                deplacer(pos1, pos2, echiquier)                                    # Déplacer la pièce du point A au point B
            else:                                                              # Sinon :
                print("Tu ne peux pas déplacer le Roi Noir ici")                   # Afficher message d'erreur
    else:                                                              # Sinon :
        print("Tu ne peux pas manger une pièce à toi !")                   # Afficher message d'erreur

def chess():
    echiquier = []                                         # Tableau représentant l'échiquier
    fin_partie = False                                     # Faux tant que la partie continue
    joueur1 = input("Nom Joueur 1 : ")                     # Demande le nom du Joueur 1
    joueur2 = input("Nom Joueur 2 : ")                     # Demande le nom du Joueur 2
    prochain_tour = joueur1                                # Donne le tour au Joueur 1
    creer_echiquier(echiquier)                             # Génère un échiquier
    afficher_echiquier(echiquier)                          # Affiche l'échiquier sur la console
    while fin_partie == False:                             # Tant que la partie continue :
        pos1 = input("Quelle pièce veux-tu jouer : ")          # Demander quelle pièce jouer
        pos2 = input("Où veux-tu déplacer cette pièce : ")     # Demander où la déplacer
        deplacement(pos1, pos2, echiquier)                     # Effectuer le déplacer
        tour_joueur(joueur1, joueur2, prochain_tour)           # Changer de tour
        afficher_echiquier(echiquier)                          # Afficher l'échiquier

if __name__ == "__main__":
    chess()