import numpy as np
import matplotlib.pyplot as plt
from functions import *
from utils import *

# Momentum gradient descent
def momentumGradientDescent(x_0, function, gamma=0.9, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]
    listeVariation = [np.array([0 for i in range(dim)])]

    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        variation = function.gradient(currentX, h) * learningRate + gamma*listeVariation[i]
        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
        listeVariation.append(np.copy(variation))

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    return np.array(listeX)

# Batch gradient descent
def batchGradientDescent(x_0, function, learningRate=0.01, maxIter=1000):
    """ The gradient descent classic algorithm """
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]

    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        variation = function.gradient(currentX, h) * learningRate
        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    return np.array(listeX)


# Nesterov gradient descent
def nesterovGradientDescent(x_0, function, gamma=0.9, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]
    listeVariation = [np.array([0 for i in range(dim)])]

    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        variation = function.gradient(currentX-gamma*listeVariation[i], h) * learningRate + gamma*listeVariation[i]
        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
        listeVariation.append(np.copy(variation))

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    return np.array(listeX)
    

# Adagrad gradient descent
def adagradGradientDescent(x_0, function, learningRate=0.01, maxIter=400):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]
    
    # Initiliasation de Gt (somme des carrées des gradients trouvé jusqu'à lors pour chaque paramètre)
    squareGradient = np.array([0e-8 for i in range(dim)])

    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        
        gradient = function.gradient(currentX, h)
        squareGradient += gradient ** 2
        variation = (gradient/ np.sqrt(squareGradient))*learningRate

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
        if i % 500 == 0:
            
            utils.vprint("Itération {} : {}".format(i, currentX ))
            
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    return np.array(listeX)

# Adadelta gradient descent
def adadeltaGradientDescent(x_0, function, gamma=0.9, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX), np.copy(currentX)]
    
    # Initialisation de E[g] et E[O]
    squareGradient = np.array([1e-8 for i in range(dim)])
    squareParameterVariation = np.array([1 for i in range(dim)])
    
    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        
        gradient = function.gradient(currentX, h)
        
        squareGradient = gamma*squareGradient +(1-gamma)* gradient**2
        squareParameterVariation = gamma*squareParameterVariation + (1-gamma)* (listeX[-1]-listeX[-2])**2
        
        variation = (np.sqrt(squareParameterVariation)/ np.sqrt(squareGradient))*gradient

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            
            utils.vprint("Itération {} : {}".format(i, currentX ))

    return np.array(listeX)
    
"""
Lancement du programme
"""
if __name__ == '__main__':
    batchGradientDescent([0], square)
    momentumGradientDescent([0], square)
    nesterovGradientDescent([0], square)
    adagradGradientDescent([0], square)
    adadeltaGradientDescent([0], square)
