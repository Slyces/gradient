import numpy as np
import matplotlib.pyplot as plt

"""
Descente du gradient momentum (Ajout d'un parametre gamma)
"""
def momentumGradientDescent(function, dimension, xInit, learningRate, gamma=0.9, maxIter=10000):
    currentX = xInit # np.array
    print(currentX)
    listeX = [currentX] # Initialisation de la liste des valeurs trouvées
    listeGradient = [np.array([0 for i in range(dimension)])] # Initialisation du gradient a 0
    n = 0.0001 # Variation nécéssaire au calcul du gradient

    # On limite le nombre d'itération
    for i in range(maxIter):

        gradient = np.array([])
        # Calcul du gradient pour chaque dimension
        for j in range(dimension):
            # Création de la variation
            liste = [0 for k in range(dimension)]
            liste[j] = n
            gradJ = ((function(currentX+np.array(liste)))-function(currentX))/n
            gradient = np.append(gradient, [learningRate * gradJ])


        """ C'est ici que ça change """
        gradient = gamma*listeGradient[i] + gradient # On change le gradient avec une direction lié au précédent


        listeGradient.append(gradient) # On a ajoute le gradient au valeurs connu
        currentX = currentX - gradient # Modification de X

        if i % 500 == 0:
            print(currentX)
        listeX.append(currentX) # On garde la valeur de x en mémoire

    return currentX

"""
Descente du gradient classique
"""
def batchGradientDescent(function, dimension, xInit, learningRate, maxIter=10000):
    currentX = xInit # np.array
    print(currentX)
    listeX = [currentX] # Initialisation de la liste des valeurs trouvées
    listeGradient = [np.array([0 for i in range(dimension)])] # Initialisation du gradient a 0
    n = 0.0001 # Variation nécéssaire au calcul du gradient
    gradient = np.array([])
    # On limite le nombre d'itération
    for i in range(maxIter):
        gradient = np.array([])
        # Calcul du gradient pour chaque dimension
        for j in range(dimension):
            # Création de la variation
            liste = [0 for k in range(dimension)]
            liste[j] = n
            gradJ = ((function(currentX+np.array(liste)))-function(currentX))/n
            gradient = np.append(gradient, [learningRate * gradJ])

        listeGradient.append(gradient) # On a ajoute le gradient au valeurs connu
        currentX = currentX - gradient # Modification de X

        if i % 500 == 0:
            print(currentX)
        listeX.append(currentX) # On garde la valeur de x en mémoire

    return currentX

"""
Descente du gradient stochastique
"""
def stochastiqueGradientDescent(function, dimension, xInit, learningRate, maxIter=10000):
    currentX = xInit # np.array
    print(currentX)
    listeX = [currentX] # Initialisation de la liste des valeurs trouvées
    listeGradient = [np.array([0 for i in range(dimension)])] # Initialisation du gradient a 0
    n = 0.0001 # Variation nécéssaire au calcul du gradient

    # On limite le nombre d'itération
    for i in range(maxIter):

        # Calcul du gradient pour chaque dimension et modification de X
        for j in range(dimension):
            # Création de la variation
            gradient = [0 for k in range(dimension)]
            gradient[j] = n
            gradJ = ((function(currentX+np.array(gradient)))-function(currentX))/n
            gradient[j] = learningRate * gradJ
            gradient = np.array(gradient)

            listeGradient.append(gradient) # On a ajoute le gradient au valeurs connu
            currentX = currentX - gradient # Modification de X
        if i % 500 == 0:
            print(currentX)
        listeX.append(currentX) # On garde la valeur de x en mémoire

    return currentX


"""
Baele function
Input : x, y
Output : real
"""
def baeleFunction(liste):
    x = liste[0]
    y = liste[1]
    return (1.5 -x +x*y)**2 + (2.25-x+x*y**2)**2 + (2.625 - x +x*y**3)**2

"""
Booth function
Input : x, y
Output : real
"""
def boothFunction(liste):
    x = liste[0]
    y = liste[1]
    return (x+2*y-7)**2 + (2*x+y-5)**2

"""
Lancement du programme
"""
if __name__ == '__main__':
    momentumGradientDescent(boothFunction, 2, np.array([0, 0]), 0.001)
