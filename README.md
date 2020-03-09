# TP  sur le jeu de la vie
Le jeu de la vie est un automate céllulaire mis au point par John Horton Conway.
Dans ce TP, nous avons implémenté de deux manières différentes (avec et sans numpy) le jeu de la vie.
 
# Règles du jeu
Nous partons initialement d'une grille bidimensionnelle de taille finie carrée.
On suppose que le pourtour de la grille est toujours inactif/mort et que les cellules du jeu ne peuvent prendre qu'un seul état parmi les   états morts(0) et vivants (1). Chaque cellule de la grille intéragit avec ses 8 cellules voisines.
Voici ci-dessus les transitions possibles à chaque étape :
- Toute cellule morte ayant exactement 3 voisins vivants devient une cellule vivante (naissance)
- Toute cellule vivante avec 2 ou 3 voisins vivants reste vivante à la génération suivante (équilibre)
- Toute cellule vivante ayant 4 voisins vivants meurt à la génération suivante (mort par étouffement)
- Toute cellule vivante ayant 0 ou 1 voisin vivant décède à la génération suivante (mort par isolement)

 
 
 

