import variables
import dictionnaires
import time

def timer(joueur1, joueur2, nb_tour, temps):
    """Compte à rebours indiquant le temps qu'il reste au joueur
    
    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        nb_tour (int): Nombre de tour
        temps (int): Durée arbitraire du temps attribué
    
    Returns:
        (str): Temps restant du joueur
    """
    temps_depart = time.time()                                         # Définit le temps de départ à partir de l'heure Unix
    temps_fin = temps_depart + temps                                   # Ajoute le temps saisi par les joueurs à l'heure Unix
    temps_joueur1 = temps                                              # Tempt du joueur 1
    temps_joueur2 = temps                                              # Temps du joueur 2
    if nb_tour % 2 == 1:                                               # Si le tour est impair donc au joueur 1 :
        while 0 < temps_joueur1:                                           # Temps que le temps du joueur 1 n'est pas écoulé :
            time.sleep(1)                                                       # Retirer une seconde
            temps_joueur1 = int(temps_fin - time.time())                        # Retire l'heure Unix pour avoir le vrai temps écoulé
            return ("Il reste", temps_joueur1, "secondes à", joueur1)           # Affiche le temps restant du joueur 1
    elif nb_tour % 2 == 0:                                            # Si tour est pair donc au joueur 2 :
        while 0 < temps_joueur2:                                           # Temps que le temps du joueur 2 n'est pas écoulé :
            time.sleep(1)                                                       # Retirer une seconde
            temps_joueur2 = int(temps_fin - time.time())                        # Retire l'heure Unix pour avoir le vrai temps écoulé
            return ("Il reste", temps_joueur2, "secondes à", joueur2)           # Affiche le temps restant du joueur 2

def tour_joueur(joueur1, joueur2, nb_tour):
    """Système de tour par tour

    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        nb_tour (int): Nombre de tour
    """
    if nb_tour % 2 == 1:             # Si tour est impair :
        print("Tour de :", joueur1)      # Indique à qui est le tour
    elif nb_tour % 2 == 0:           # Si tour est pair :
        print(f"Tour de :", joueur2)     # Indique à qui est le tour

def match_nul(joueur1, joueur2, nb_tour, echiquier):
    """Propose un match nul au joueur adverse et gère sa réponse
    
    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        nb_tour (int): Nombre de tours
        prochain_tour (str): Nom du joueur ayant le droit de jouer
    
    Returns:
        (bool): Vrai ou Faux
    """
    if nb_tour % 2 == 1:                                                    # Si la fonction est appelée par le Joueur 1 :
        reponse = input(joueur2, "acceptes-tu le match nul ? (Oui/Non) : ")     # Demande à l'adversaire s'il accepte
        if reponse.upper() == "OUI":                                            # Si oui :
            print("Match nul !")                                                    # Match Nul
            creer_echiquier(echiquier)                                              # Réinitialise l'échiquier
            return True                                                             # Indique que la partie est nulle
        else:                                                                   # Sinon :
            print("Le match nul est refusé. La partie continue.")                   # Match nul refusé
            return False                                                            # Indique que la partie reprend
    elif nb_tour % 2 == 0:                                                  # Si la fonction est appelée par le Joueur 2 :
        reponse = input(joueur1, "acceptes-tu le match nul ? (Oui/Non) : ")     # Demande à l'adversaire s'il accepte
        if reponse.upper() == "OUI":                                            # Si oui :
            print("Match nul !")                                                    # Match nul
            creer_echiquier(echiquier)                                              # Réinitialise l'échiquier
            return True                                                             # Indique que la partie est nulle
        else:                                                                   # Sinon :
            print("Le match nul est refusé. La partie continue.")                   # Match nul refusé
            return False                                                            # Indique que la partie reprend

def forfait(joueur1, joueur2, nb_tour, echiquier):
    """Déclare forfait et réinitialise l'échiquier
    
    Args:
        joueur1 (str): Nom du Joueur 1
        joueur2 (str): Nom du Joueur 2
        nb_tour (str): Nombre de tour
        echiquier (list): Tableau à 2 dimensions
    
    Returns:
        (bool): Vrai ou Faux
    """
    if nb_tour % 2 == 1:                    # Si le Joueur 1 a déclaré forfait :
        print(joueur1, "a déclaré forfait")     # Indique qu'il déclare forfait
        creer_echiquier(echiquier)              # Réinitialise l'échiquier
        return True                             # Renvoyer Vrai
    elif nb_tour % 2 == 0:                  # Si le Joueur 2 a déclaré forfait :
        print(joueur2, "a déclaré forfait")     # Indique qu'il déclare forfait
        creer_echiquier(echiquier)              # Réinitialise l'échiquier  
        return True                             # Renvoyer Vrai
    else:                                   # Sinon :
        return False                            # Renvoyer Faux

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
    caractere = caractere.upper()
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

def verif(liste, point):
    """Vérifie que le point existe

    Args:
        list (list): Représente toute les valeurs possible à l'axe
        point (int): Une des deux oordonnées du point B

    Returns:
        (bool): Vrai ou Faux
    """
    for v in liste :    # Pour chaque valeur présente dans liste :
        if point == v :     # Si va est présent dans la liste :
            return True         # Renvoyer Vrai
    return False        # Sinon renvoyer Faux

def reco_coordonnees(coordonnees):
    """Interprète une chaine de caractère pour déterminer la position dans le dictionnaire

    Args:
        coordonnees (str): Indices x et y de l'échiquier
    
    Returns:
        (dict): Dictionnaire à 1 dimension
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

def recup_coordonnees(pos, echiquier):
    """Récupère les coordonnées à partir d'indices du tableau

    Args:
        pos (str): Valeur du tableau
        echiquier (list): Tableau à 2 dimensions
        
    Returns:
        (str): str à 2 caractères
    """
    for lettre in dictionnaires.coords:                                                                                  # Pour chaque lettre :
        for chiffre in dictionnaires.coords[lettre]:                                                                         # Pour chaque chiffre :                                                         
            if echiquier[dictionnaires.coords[lettre][chiffre]["x"]][dictionnaires.coords[lettre][chiffre]["y"]] == pos:         # Si les valeurs trouvé dans le tableau sont identiques que celle de la position :
                return lettre+chiffre                                                                                                # Renvoyer str contenant la coordonnée correspondant au indices du tableau

def obstacle_h(pos1, pos2, echiquier):
    """Détecte si une pièce est présente dans la trajectoire du fou

    Args:
        pos1 (dict): Indices du tableau du point A
        pos2 (dict): Indices du tableau du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    if pos2.get("y") > pos1.get("y"):        # Si y2 est plus grand que y1 :
        ligne_h = 2                              # y = 2
    else:                                    # Si y1 est plus grand que y2 :
        ligne_h = -2                             # y = -2
    ligne = pos1.get("y") + ligne_h          # Ajouter y à y1
    colonne = pos1.get("x")                  # Récupère x1
    while ligne != pos2.get("y"):            # Tant que la y1 + y est différent de y2 :
        if echiquier[colonne][ligne] != " ":     # Si la case n'est pas vide :
            return False                             # Renvoyer Faux
        ligne += ligne_h                         # Ajouter y à y1
    return True                              # Renvoyer Vrai

def obstacle_v(pos1, pos2, echiquier):
    """Détecte si une pièce est présente dans la trajectoire du fou

    Args:
        pos1 (dict): Indices du tableau du point A
        pos2 (dict): Indices du tableau du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    if pos2.get("x") > pos1.get("x"):        # Si x2 est plus grand que x1 :
        colonne_v = 2                            # x = 2
    else:                                    # Si x1 est plus grand que x2 :
        colonne_v = -2                           # x = -2
    ligne = pos1.get("y")                    # Récupère y1
    colonne = pos1.get("x") + colonne_v      # Ajouter x à x1
    while colonne != pos2.get("x"):          # Tant que la x1 + x est différent de x2 :
        if echiquier[colonne][ligne] != " ":     # Si la case n'est pas vide :
            return False                             # Renvoyer Faux
        colonne += colonne_v                     # Ajouter y à y1
    return True                              # Renvoyer Vrai

def obstacle_d(pos1, pos2, echiquier):
    """Détecte si une pièce est présente dans la trajectoire du fou

    Args:
        pos1 (dict): Indices du tableau du point A
        pos2 (dict): Indices du tableau du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    if pos2.get("y") > pos1.get("y"):            # Si y2 est plus grand que y1 :
        ligne_h = 2                                  # y = 2
    else:                                        # Si y1 est plus grand que y2 :
        ligne_h = -2                                 # y = -2
    if pos2.get("x") > pos1.get("x"):            # Si x2 est plus grand que x1 :
        colonne_v = 2                                # x = 2
    else:                                        # Si x1 est plus grand que x2 :
        colonne_v = -2                               # x = -2
    ligne = pos1.get("y") + ligne_h              # Ajouter y à y1
    colonne = pos1.get("x") + colonne_v          # Ajouter x à x1
    while ligne != pos2.get("y"):                # Tant que la y1 + y est différent de y2 :
        while colonne != pos2.get("x"):              # Tant que la x1 + x est différent de x2 :
            if echiquier[colonne][ligne] != " ":         # Si la case n'est pas vide :
                return False                             # Renvoyer Faux
            ligne += ligne_h                         # Ajouter y à y1
            colonne += colonne_v                     # Ajouter y à y1
    return True                                  # Renvoyer Vrai

def condition_pion(pos1, pos2, echiquier):
    """Conditionne le déplacement du pion

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions
        
    Returns: 
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                                                                      # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                                                                      # Récupère les indices de l'échiquier correspondant au point B
    piece = echiquier[pos1.get("x")][pos1.get("y")]                                                    # Récupère la pièce se trouvant au point A
    if piece == variables.pion_b:                                                                      # Si le pion est blanc :
        if echiquier[pos2.get("x")+2][pos2.get("y")] == echiquier[pos1.get("x")][pos1.get("y")]:           # Si x2 + 2 = x1 et y2 = y1 :
            return True                                                                                        # Renvoyer Vrai
        if echiquier[pos2.get("x")+2][pos2.get("y")-2] == echiquier[pos1.get("x")][pos1.get("y")]:         # Si x2 + 2 = x1 et y2 - 2 = y1 :
            if verif(variables.noir, echiquier[pos2.get("x")][pos2.get("y")]):                                 # Si le point B est une pièce adverse :
                return True                                                                                        # Renvoyer Vrai
        if piece != echiquier[pos1.get("x")][17]:                                                          # Si le pion n'est pas en H
            if echiquier[pos2.get("x")+2][pos2.get("y")+2] == echiquier[pos1.get("x")][pos1.get("y")]:         # Si x2 + 2 = x1 et y2 + 2 = y1 :
                if verif(variables.noir, echiquier[pos2.get("x")][pos2.get("y")]):                                 # Si le point B est une pièce adverse :
                    return True                                                                                       # Renvoyer Vrai
        elif echiquier[pos2.get("x")+4][pos2.get("y")] == echiquier[13][pos1.get("y")]:                    # Si x2 + 4 = 13 et y2 = y1 :
            return True                                                                                        # Renovyer Vrai
    elif piece == variables.pion_n:                                                                    # Si le pion est noir :
        if echiquier[pos2.get("x")-2][pos2.get("y")] == echiquier[pos1.get("x")][pos1.get("y")]:           # Si x2 - 2 = x1 et y2 = y1 :
            return True                                                                                        # Renvoyer Vrai
        if echiquier[pos2.get("x")-2][pos2.get("y")-2] == echiquier[pos1.get("x")][pos1.get("y")]:         # Si x2 - 2 = x1 et y2 - 2 = y1 :
            if verif(variables.blanc, echiquier[pos2.get("x")][pos2.get("y")]):                                # Si le point B est une pièce adverse :
                return True                                                                                        # Renvoyer Vrai
        if piece != echiquier[pos1.get("x")][17]:                                                          # Si le pion n'est pas en H
            if echiquier[pos2.get("x")-2][pos2.get("y")+2] == echiquier[pos1.get("x")][pos1.get("y")]:         # Si x2 - 2 = x1 et y2 + 2 = y1 :
                if verif(variables.blanc, echiquier[pos2.get("x")][pos2.get("y")]):                                # Si le point B est une pièce adverse :
                    return True                                                                                        # Renvoyer Vrai
        elif echiquier[pos2.get("x")-4][pos2.get("y")] == echiquier[3][pos1.get("y")]:                     # Si x2 - 4 = 3 et y2 = y1 :
            return True                                                                                        # Renvoyer Vrai
    return False                                                                                        # Renvoyer Faux

def condition_tour(pos1, pos2, echiquier):
    """Conditionne le déplacement de la tour en vertical

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions
        
    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                            # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                            # Récupère les indices de l'échiquier correspondant au point B
    if pos2.get("y") == pos1.get("y"):                       # Si y2 = y1 :
        if verif(variables.colonne, pos2.get("x")) == True:      # Si x2 se situe dans les x utilisables :
            if obstacle_v(pos1, pos2, echiquier) == True:            # Si aucune pièce est présente sur la trajectoire de la tour :
                return True                                              # Renvoyer Vrai
    elif pos2.get("x") == pos1.get("x"):                     # Si x2 = x1 :
        if verif(variables.ligne, pos2.get("y")) == True:        # Si y2 se situe dans les y utlisables :
            if obstacle_h(pos1, pos2, echiquier) == True:            # Si aucune pièce est présente sur la trajectoire de la tour :
                return True                                              # Renvoyer Vrai
    return False                                             # Renvoyer Faux

def condition_fou(pos1, pos2, echiquier):
    """Conditionne le déplacement du fou

    Args:
        pos1 (str): Coordonnées du point A
        pos2 (str): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    pos1 = reco_coordonnees(pos1)                   # Récupère les indices de l'échiquier correspondant au point A
    pos2 = reco_coordonnees(pos2)                   # Récupère les indices de l'échiquier correspondant au point B
    x = abs(pos2.get("x") - pos1.get("x"))          # Valeur absolue de x2 - x1
    y = abs(pos2.get("y") - pos1.get("y"))          # Valeur absolue de y2 - y1
    if x != y:                                      # Si x est différent de y :
        return True                                     # Renvoyer Vrai
    elif obstacle_d(pos1, pos2, echiquier) == True: # Si une pièce est présente sur la trajectoire du fou :
        return False                                    # Renvoyer Faux

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


def deplacement(pos1, pos2, tour, echiquier):
    """Autorise les pièces à se déplacer si elles respectent les conditions requises

    Args:
        pos1 (int): Coordonnées du point A
        pos2 (int): Coordonnées du point B
        echiquier (list): Tableau à 2 dimensions
    """
    piece = reco_coordonnees(pos1)                                         # Récupère les indices de l'échiquier correspondant au point A
    piece = echiquier[piece.get("x")][piece.get("y")]                      # Récupère la valeur du point A
    if reco_allies(pos1, pos2, echiquier) == False:                        # Si les pièces au point A et au point B ne dans le même camp :
        if tour % 2 == 1:                                                      # Si le tour est au Joueur 1
            if piece == variables.pion_b:                                          # Si la pièce déplacée est un Pion Blanc :
                if condition_pion(pos1, pos2, echiquier) == True:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                                                                                           # Non terminé (il manque, le "en passant")
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Pion Blanc ici")                     # Afficher message d'erreur
            elif piece == variables.tour_b:                                        # Si la pièce déplacée est un Tour Blanc :
                if condition_tour(pos1, pos2, echiquier) == True:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Tour Blanche ici")                   # Afficher message d'erreur
            elif piece == variables.fou_b:                                         # Si la pièce déplacée est un Fou Blanc :
                if condition_fou(pos1, pos2, echiquier) == False:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Fou Blanc ici")                      # Afficher message d'erreur
            elif piece == variables.reine_b:                                       # Si la pièce déplacée est un Reine Blanc :
                if condition_fou(pos1, pos2, echiquier) == False:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                elif condition_tour(pos1, pos2, echiquier) == True:                    # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer la Reine Blanche ici")                  # Afficher message d'erreur
            elif piece == variables.cavalier_b:                                    # Si la pièce déplacée est un Cavalier Blanc :
                if condition_cavalier(pos1, pos2) == True:                             # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Cavalier Blanc ici")                 # Afficher message d'erreur
            elif piece == variables.roi_b:                                         # Si la pièce déplacée est un Roi Blanc :
                if condition_roi(pos1, pos2) == True:                                  # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Roi Blanc ici")                      # Afficher message d'erreur
        elif tour % 2 == 0:                                                    # Si le tour est au Joueur 2
            if piece == variables.pion_n:                                          # Si la pièce déplacée est un Pion Noir :
                if condition_pion(pos1, pos2, echiquier) == True:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                                                                                           # Non terminé (il manque, le "en passant")
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Pion Noir ici")                      # Afficher message d'erreur
            elif piece == variables.tour_n:                                        # Si la pièce déplacée est un Tour Noir :
                if condition_tour(pos1, pos2, echiquier) == True:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Tour Noir ici")                      # Afficher message d'erreur
            elif piece == variables.fou_n:                                         # Si la pièce déplacée est un Fou Noir :
                if condition_fou(pos1, pos2, echiquier) == False:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Fou Noir ici")                       # Afficher message d'erreur
            elif piece == variables.reine_n:                                       # Si la pièce déplacée est un Reine Noir :
                if condition_fou(pos1, pos2, echiquier) == False:                      # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                elif condition_tour(pos1, pos2, echiquier) == True:                    # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer la Reine Noire ici")                    # Afficher message d'erreur
            elif piece == variables.cavalier_n:                                    # Si la pièce déplacée est un Cavalier Noir :
                if condition_cavalier(pos1, pos2) == True:                             # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Cavalier Noir ici")                  # Afficher message d'erreur
            elif piece == variables.roi_n:                                         # Si la pièce déplacée est un Roi Noir :
                if condition_roi(pos1, pos2) == True:                                  # Si les conditions sont vérifiées :
                    deplacer(pos1, pos2, echiquier)                                        # Déplacer la pièce du point A au point B
                else:                                                                  # Sinon :
                    print("Tu ne peux pas déplacer le Roi Noir ici")                       # Afficher message d'erreur
    else:                                                              # Sinon :
        print("Tu ne peux pas manger une pièce à toi !")                   # Afficher message d'erreur

def detection_h(pos1, pos2, echiquier):
    """Détecte si une pièce est présente dans la trajectoire horizontale de la tour

    Args:
        pos1 (dict): Indices du tableau du point A
        pos2 (dict): Indices du tableau du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    if pos2.get("y") > pos1.get("y"):        # Si y2 est plus grand que y1 :
        ligne_h = 2                              # y = 2
    else:                                    # Si y1 est plus grand que y2 :
        ligne_h = -2                             # y = -2
    ligne = pos1.get("y") + ligne_h          # Ajouter y à y1
    colonne = pos1.get("x")                  # Récupère x1
    while ligne != pos2.get("y"):            # Tant que la y1 + y est différent de y2 :
        if echiquier[colonne][ligne] != " ":     # Si la case n'est pas vide :
            return False                             # Renvoyer Faux
        ligne += ligne_h                         # Ajouter y à y1
    return True                              # Renvoyer Vrai

def detection_v(pos1, pos2, echiquier):
    """Détecte si une pièce est présente dans la trajectoire verticale de la tour

    Args:
        pos1 (dict): Indices du tableau du point A
        pos2 (dict): Indices du tableau du point B
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    if pos2.get("x") > pos1.get("x"):        # Si x2 est plus grand que x1 :
        colonne_v = 2                            # x = 2
    else:                                    # Si x1 est plus grand que x2 :
        colonne_v = -2                           # x = -2
    ligne = pos1.get("y")                    # Récupère y1
    colonne = pos1.get("x") + colonne_v      # Ajouter x à x1
    while colonne != pos2.get("x"):          # Tant que la x1 + x est différent de x2 :
        if echiquier[colonne][ligne] != " ":     # Si la case n'est pas vide :
            return False                             # Renvoyer Faux
        colonne += colonne_v                     # Ajouter y à y1
    return True                              # Renvoyer Vrai

def fou_n_roi(echiquier, roi):
    """Vérifie si le fou noir fait echec avec le roi blanc

    Args:
        echiquier (liste): L'echiquier
        roi (str): la position roi

    Returns:
        (bool): True si le fou fait echec avec le roi sinon False 
    """
    r_b = reco_coordonnees(recup_coordonnees(variables.roi_b, echiquier)) 
    pos3 = reco_coordonnees(recup_coordonnees(variables.fou_n, echiquier))
    if roi == variables.roi_b:
        if (r_b.get("y") - pos3.get("y")) > 0:
            ligne_d_1 = 2
        else:
            ligne_d_1 = -2                                # direction de la diagonale
        if (r_b.get("x") - pos3.get("x")) > 0:
            colonne_d_1 = 2
        else:
            colonne_d_1 = -2                              # direction de la diagonale
        ligne_1 = pos3.get("y")
        colonne_1 = pos3.get("x")
        while (ligne_1 != r_b.get("y")) and (colonne_1 != r_b.get("x")):
            ligne_1 += ligne_d_1
            colonne_1 += colonne_d_1
            if verif(variables.pieces_sans_roi, echiquier[colonne_1][ligne_1]): #a = les autres pièce que le roi
                return False
            elif echiquier[colonne_1][ligne_1] == echiquier[r_b.get("x")][r_b.get("y")]:
                return True
            
def reine_n_roi(echiquier, roi):
    """Vérifie si le reine noir fait echec avec le roi blanc

    Args:
        echiquier (liste): L'echiquier
        roi (str): la position roi

    Returns:
        (bool): True si reine noir fait echec avec le roi sinon False 
    """
    r_b = reco_coordonnees(recup_coordonnees(variables.roi_b, echiquier)) 
    pos4 =reco_coordonnees(recup_coordonnees(variables.reine_n, echiquier))
    if roi == variables.roi_b:
        if (r_b.get("y") - pos4.get("y")) > 0:
                ligne_d_2 = 2
        else:
                ligne_d_2 = -2                                # direction de la diagonale
        if (r_b.get("x") - pos4.get("x")) > 0:
                colonne_d_2 = 2
        else:
                colonne_d_2 = -2                              # direction de la diagonale            ligne_2 = pos4.get("y")
        colonne_2 = pos4.get("x")
        ligne_2 = pos4.get("y")
        while (ligne_2 != r_b.get("y")) and (colonne_2 != r_b.get("x")):
            ligne_2 += ligne_d_2
            colonne_2 += colonne_d_2
            if verif(variables.pieces_sans_roi, echiquier[colonne_2][ligne_2]): #a = les autres pièce que le roi
                return False
            elif echiquier[colonne_2][ligne_2] == echiquier[r_b.get("x")][r_b.get("y")]:
                return True

def fou_b_roi(echiquier, roi):
    """Vérifie si le fou blancs fait echec avec le roi noir

    Args:
        echiquier (liste): L'echiquier
        roi (str): la position roi

    Returns:
        (bool): True si fou blanc fait echec avec le roi sinon False 
    """
    r_n = reco_coordonnees(recup_coordonnees(variables.roi_n, echiquier))
    pos1 = reco_coordonnees(recup_coordonnees(variables.fou_b, echiquier))
     
    if roi == variables.roi_n:
        if (r_n.get("y") - pos1.get("y")) > 0:
            ligne_d_3 = 2
        else:
            ligne_d_3 = -2                                # direction de la diagonale
        if (r_n.get("x") - pos1.get("x")) > 0:
            colonne_d_3 = 2
        else:
            colonne_d_3 = -2                              # direction de la diagonale
        ligne_3 = pos1.get("y")
        colonne_3 = pos1.get("x")
        while (ligne_3 != r_n.get("y")) and (colonne_3 != r_n.get("x")):
            ligne_3 += ligne_d_3
            colonne_3 += colonne_d_3
            if verif(variables.pieces_sans_roi, echiquier[colonne_3][ligne_3]): #a = les autres pièce que le roi
                return False
            elif echiquier[colonne_3][ligne_3] == echiquier[r_n.get("x")][r_n.get("y")]:
                return True

def reine_b_roi(echiquier, roi):
    """Vérifie si le reine blanche fait échec avec le roi noir

    Args:
        echiquier (list): Tableau à 2 dimensions
        roi (str): Position du roi 

    Returns:
        (bool): Vrai ou Faux
    """
    r_n = reco_coordonnees(recup_coordonnees(variables.roi_n, echiquier))
    pos2 = reco_coordonnees(recup_coordonnees(variables.reine_b, echiquier))
     
    if roi == variables.roi_n:
        if (r_n.get("y") - pos2.get("y")) > 0:
            ligne_d_4 = 2
        else:
            ligne_d_4 = -2                                # direction de la diagonale
        if (r_n.get("x") - pos2.get("x")) > 0:
            colonne_d_4 = 2
        else:
            colonne_d_4 = -2                              # direction de la diagonale
        ligne_4 = pos2.get("y")
        colonne_4 = pos2.get("x")
        while (ligne_4 != r_n.get("y")) and (colonne_4 != r_n.get("x")):
            ligne_4 += ligne_d_4
            colonne_4 += colonne_d_4
            if verif(variables.pieces_sans_roi, echiquier[colonne_4][ligne_4]): #a = les autres pièce que le roi
                return False
            elif echiquier[colonne_4][ligne_4] == echiquier[r_n.get("x")][r_n.get("y")]:
                return True
            
def detection_fou(echiquier, roi):
    """Détecte si une pièce est présente dans la trajectoire du fou

    Args:
        roi (str): Valeur du tableau correspondant à l'un des deux rois
        echiquier (list): Tableau à 2 dimensions

    Returns:
        (bool): Vrai ou Faux
    """
    if roi == variables.roi_b :
        if fou_n_roi(echiquier, roi) == True or reine_n_roi(echiquier, roi) == True:
            return True
    if roi == variables.roi_n :
       if fou_b_roi(echiquier, roi) == True or reine_b_roi(echiquier, roi) == True:
            return True
    return False

def detection_cavalier(echiquier):
    """Détecte si le cavalier met en echec le roi

    Args:
        echiquier (list): Tableau à deux dimensions

    Returns:
        bool: Vrai ou Faux
    """
    for x in range(len(echiquier)):
        for y in range(len(echiquier[x])):
            if echiquier[x][y] == variables.roi_b:
                for i in [-2, -1, 1, 2]:
                    for j in [-2, -1, 1, 2]:
                        if abs(i) != abs(j):  # Exclure les déplacements en diagonale
                            if x + i >= 0 and x + i < 8 and y + j >= 0 and y + j < 8:
                                if echiquier[x + i][y + j] == variables.cavalier_n:
                                    return True
            elif echiquier[x][y] == variables.roi_n:
                for i in [-2, -1, 1, 2]:
                    for j in [-2, -1, 1, 2]:
                        if abs(i) != abs(j):  # Exclure les déplacements en diagonale
                            if x + i >= 0 and x + i < 8 and y + j >= 0 and y + j < 8:
                                if echiquier[x + i][y + j] == variables.cavalier_b:
                                    return True

def detection_tour(echiquier):
    for x in range(len(echiquier)):
        for y in range(len(echiquier[x])):
            if echiquier[x][y] == variables.roi_b:
                for l in variables.ligne:
                    if echiquier[l][y] == variables.tour_n:
                        if detection_h(reco_coordonnees(recup_coordonnees(echiquier[l][y], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
                    elif echiquier[l][y] == variables.reine_n:
                        if detection_h(reco_coordonnees(recup_coordonnees(echiquier[l][y], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
                for c in variables.colonne:
                    if echiquier[x][c] == variables.tour_n:
                        if detection_v(reco_coordonnees(recup_coordonnees(echiquier[x][c], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
                    elif echiquier[x][c] == variables.reine_n:
                        if detection_v(reco_coordonnees(recup_coordonnees(echiquier[x][c], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
            elif echiquier[x][y] == variables.roi_n:
                for l in variables.ligne:
                    if echiquier[l][y] == variables.tour_b:
                        if detection_h(reco_coordonnees(recup_coordonnees(echiquier[l][y], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
                    elif echiquier[l][y] == variables.reine_b:
                        if detection_h(reco_coordonnees(recup_coordonnees(echiquier[l][y], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
                for c in variables.colonne:
                    if echiquier[x][c] == variables.tour_b:
                        if detection_v(reco_coordonnees(recup_coordonnees(echiquier[c][y], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True
                    elif echiquier[x][c] == variables.reine_b:
                        if detection_v(reco_coordonnees(recup_coordonnees(echiquier[c][y], echiquier)), reco_coordonnees(recup_coordonnees(echiquier[x][y], echiquier)), echiquier) == False:
                            return True

def chess():
    echiquier = []                                                                                # Tableau représentant l'échiquier
    fin_partie = False                                                                            # Faux tant que la partie continue
    joueur1 = input("Nom Joueur 1 : ")                                                            # Demande le nom du Joueur 1
    joueur2 = input("Nom Joueur 2 : ")                                                            # Demande le nom du Joueur 2
    nb_tour = 1                                                                                   # Nombre de tour
    temps = int(input("Combien de secondes chaque joueur possède ? : "))                          # Temps de jeu
    creer_echiquier(echiquier)                                                                    # Génère un échiquier
    while fin_partie == False:                                                                    # Tant que la partie continue :
        afficher_echiquier(echiquier)                                                                 # Afficher l'échiquier
        tour_joueur(joueur1, joueur2, nb_tour)                                                        # Afficher le premier tour
        print("Vous êtes au tour : ", nb_tour)                                                        # Afficher le tour
        print(timer(joueur1, joueur2, nb_tour, temps))                                                # Afficher le temps restant 
        pos1 = input("Match nul --> 'NUL'\nForfait --> 'FORFAIT'\nQuelle pièce veux-tu jouer : ")     # Pièce à déplacer / Match Nul / Forfait 
        pos2 = input("Où veux-tu déplacer cette pièce : ")                                            # Demander où la déplacer
        if pos1.upper() == "NUL":                                                                     # Si réponse = NUL :
            if match_nul(echiquier) == True:                                                              # Si l'adversaire accepte :
                fin_partie = True                                                                             # Termine la partie
        elif pos1.upper() == "FORFAIT" :                                                              # Si réponse = NUL :
            if forfait(echiquier) == True:                                                                # Renvoyer message forfait :
                fin_partie = True                                                                             # Termine la partie
        else:                                                                                         # Sinon :
            deplacement(pos1, pos2, nb_tour, echiquier)                                                   # Effectuer le déplacement
        nb_tour += 1                                                                                  # Changer le tour
        variables.log_pos1.append(pos1)                                                               # Récupérer l'historique des pièces
        variables.log_pos2.append(pos2)                                                               # Récupérer l'historique des déplacements
        if detection_tour(echiquier) == True:                                                         # Si une tour met en echec un des roi :
            print("Tu es en échec !")                                                                     # Afficher message d'échec
        elif detection_cavalier(echiquier) == True:                                                   # Si un cavalier met en echec un des roi :
            print("Tu es en échec !")                                                                     # Afficher message d'échec
        elif detection_fou(echiquier, variables.roi_b) == True:
            print("Tu es en échec !")
        elif detection_fou(echiquier, variables.roi_n) == True:
            print("Tu es en échec !")
        if fin_partie == True:
            chess()


if __name__ == "__main__":
    chess()