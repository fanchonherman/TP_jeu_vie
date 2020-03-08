import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] \
                    + Z[x-1][y] + 0 + Z[x+1][y] \
                    + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


def affichage_iterations(mat, fonction):
    plt.figure(figsize=(10, 5))
    mat_iter = (np.array(mat))
    plt.subplot(2, 5, 1)
    plt.imshow(mat_iter)
    plt.title("itération " + "0")
    for i in range(2, 11):
        mat_iter = fonction(mat_iter)
        plt.subplot(2, 5, i)
        plt.imshow(mat_iter)
        plt.title("itération " + str(i-1))


def animation_mat(init, fonction):
    def animate(i):
        mat.set_array(fonction(init, i))
    fig, ax = plt.subplots()
    mat = ax.matshow(init)
    ani = animation.FuncAnimation(fig, animate, frames=200)
    plt.show()
    return(ani)
