pion_b = "♙"     # Dessine Pion Blanc
tour_b = "♖"     # Tour Blanche
cavalier_b = "♘" # Cavalier Blanc
fou_b = "♗"      # Fou Blanc
reine_b = "♕"    # Reine Blanche
roi_b = "♔"      # Roi Blanc
pion_n = "♟︎"     # Pion Noir
tour_n = "♜"     # Tour Noir
cavalier_n = "♞" # Cavalier Noir
fou_n = "♝"      # Fou Noir
roi_n = "♚"    # Roi Noir
reine_n = "♛"      # Reine Noir

colonne = [1,3,5,7,9,11,13,15] # Tous les indices "jouable" de l'axe y
ligne = [3,5,7,9,11,13,15,17]  # Tous les indices "jouable" de l'axe x

blanc = [pion_b, tour_b, cavalier_b, fou_b, roi_b, reine_b]                                                # Liste de toutes les pièces blanches
noir = [pion_n, tour_n, cavalier_n, fou_n, roi_n, reine_n]                                                 # Liste de toutes les pièces noires
pieces_sans_roi = [pion_n, tour_n, cavalier_n, fou_n, reine_n, pion_b, tour_b, cavalier_b, fou_b, reine_b] # Liste de toutes les pièces sans les 2 rois

log_pos1 = [] # Historique de déplacement : Position 1
log_pos2 = [] # Historique de déplacement : Position 2