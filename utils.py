def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] \
                    + Z[x-1][y] + 0 + Z[x+1][y] \
                    + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N




def iteration_jeu(Z):
    """ 
    Cette fonction prends en entrée et renvoie en sortie une liste de liste
    Les boucles ne prennent pas en compte les pourtours de la grille car
    considéré inactif/mort. En entrée on a une liste de liste qui représente l'initialisation du jeu
    En sortie on a une liste de liste qui représente le jeu à l'étape suivante
    Le code effectue les transitions a) b) c) et d) 
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1, forme[0]-1):
        for y in range(1, forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z
