import numpy as np
import matplotlib.pyplot as plt
from functions import *
import utils
from time import time


# --------------- descent object wrapping stats of the descent --------------- #
class GradientDescent(object):

    """Wrapper class containing statistics about the descent"""
    def __init__(self):
        """Void init, the descent must be completed sequentially"""
        self.points = [] # record every points of the descent
        self.variations = [] # record every variations of the point

    # ----------- getters for first and last point of the descent ------------ #
    @property
    def start(self):
        return self.points[0]

    @property
    def stop(self):
        return self.points[-1]

    # --------------------- gradually adding statistics ---------------------- #
    def add_point(self, p):
        self.points.append(p)
        pass
    
    def descent(self, x_0, function, maxIter=10000, maxTime=1e10, epsilon=1e-8):
        # Initialisation des variables communes à toutes les descentes de gradient
        self.h = 0.0001 # Variation nécéssaire au calcul du gradient
        
        
        self.x_0 = x_0 # Starting position
        self.dim = len(self.x_0) # Dimension of x_0
        self.function = function # function to minimize
        self.maxIter = maxIter # Maximum number of iteration
        self.tempsStart = time()
        self.maxTime = maxTime # Maximum time of iteration
        variation = epsilon * 10e3 # Initialisation de la variation à v > ϵ
        
        currentX = np.array(self.x_0, dtype=np.float64)
        utils.vprint("Starting position :", currentX)
        
        self.add_point(np.copy(currentX))# On garde la valeur de x en mémoire
        self.variations.append(np.copy(variation))        
        
        """ LANCEMENT DE LA DESCENTE """
        t = 0
        while t < self.maxIter and (time()-self.tempsStart) < self.maxTime and np.linalg.norm(variation) >= epsilon:
            variation  = self.getVariation(currentX)
            currentX-= variation
            self.add_point(np.copy(currentX))# On garde la valeur de x en mémoire
            self.variations.append(np.copy(variation))
            t+=1
        
        return self.points

    def getVariation(self, x):
        return self.function.gradient(x, self.h)
        


# --------------- Batch Descent --------------- #  
class BatchGradientDescent(GradientDescent):
    def __init__(self, learningRate=1e-3):
        GradientDescent.__init__(self)
        
        self.learningRate = learningRate
       
    def getVariation(self, x):
        return self.function.gradient(x, self.h)*self.learningRate

# --------------- Batch Descent --------------- #  
class MomentumGradientDescent(GradientDescent):
    def __init__(self, learningRate=1e-3, gamma=0.9):
        GradientDescent.__init__(self)
        
        self.learningRate = learningRate
        self.gamma = gamma
       
    def getVariation(self, x):
        return self.function.gradient(x, self.h)*self.learningRate + self.gamma*self.variations[-1]
    
        
        
# Momentum gradient descent
def momentumGradientDescent(x_0, function, gamma=0.9, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)
    print("momentum")
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
def batchGradientDescent(x_0, function, learningRate=0.01, maxIter=10000):
    """ The gradient descent classic algorithm """
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)
    print("batch")
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
    print(currentX)
    return np.array(listeX)


# Nesterov gradient descent
def nesterovGradientDescent(x_0, function, gamma=0.9, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)
    print("Nesterov")
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
def adagradGradientDescent(x_0, function, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    smallValues = np.array([1e-8 for i in range(dim)])

    utils.vprint("Starting position :", currentX)
    print("dadagrad")
    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]
    
    # Initiliasation de Gt (somme des carrées des gradients trouvé jusqu'à lors pour chaque paramètre)
    squareGradient = np.array([0.0 for i in range(dim)])

    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        
        gradient = function.gradient(currentX, h)
        squareGradient += gradient ** 2
        variation = (gradient/ np.sqrt(squareGradient+smallValues))*learningRate

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
            
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    print(currentX)
    return np.array(listeX)

# Adadelta gradient descent
def adadeltaGradientDescent(x_0, function, gamma=0.9, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    smallValues = np.array([1e-8 for i in range(dim)])
    utils.vprint("Starting position :", currentX)
    print("adadelta")
    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX), np.copy(currentX)]
    
    # Initialisation de E[g] et E[O]
    squareGradient = np.array([0 for i in range(dim)])
    squareParameterVariation = np.array([1e-3 for i in range(dim)])
    
    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        
        gradient = function.gradient(currentX, h)
        
        squareGradient = gamma*squareGradient +(1-gamma)* gradient**2
        squareParameterVariation = gamma*squareParameterVariation + (1-gamma)* (listeX[-1]-listeX[-2])**2
        
        variation = (np.sqrt(squareParameterVariation)/ np.sqrt(squareGradient+smallValues))*gradient

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    print(currentX)
    return np.array(listeX)

# RMSprop gradient descent
def RMSpropGradientDescent(x_0, function, gamma=0.9, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    smallValues = np.array([1e-8 for i in range(dim)])
    utils.vprint("Starting position :", currentX)
    print("RMSprop")
    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX), np.copy(currentX)]
    
    # Initialisation de E[g]
    squareGradient = np.array([0 for i in range(dim)])
    
    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        
        gradient = function.gradient(currentX, h)
        
        squareGradient = gamma*squareGradient +(1-gamma)* gradient**2        
        
        variation = (gradient*learningRate)/np.sqrt(squareGradient+smallValues)

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
    print(currentX)
    return np.array(listeX)
    
    
# Adam gradient descent
# @TODO Comprendre les beta exposant t
def adamGradientDescent(x_0, function, beta1=0.9, beta2=0.999, learningRate=0.01, maxIter=10000):
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    utils.vprint("Starting position :", currentX)
    print("Adam")
    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX), np.copy(currentX)]
      
    squareVariation = np.array([0 for i in range(dim)])
    variations = np.array([0 for i in range(dim)])
    
    # @TODO : test de convergence ϵ
    for i in range(maxIter):
        
        gradient = function.gradient(currentX, h)
        squareVariation = beta1*squareVariation + (1-beta1)*gradient
        variations = beta2*variations + (1-beta2)*gradient**2
        
        variation = (squareVariation/ np.sqrt(variations)) * learningRate

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
            print("fin", i, currentX)
            return np.array(listeX)
    return np.array(listeX)
    
"""
Lancement du programme
"""
if __name__ == '__main__':
    x = [1,0.5]
    f = sin2d
    batchGradientDescent(x, f)
    momentumGradientDescent(x, f)
    nesterovGradientDescent(x, f)
    adagradGradientDescent(x, f)
    adadeltaGradientDescent(x, f)
    RMSpropGradientDescent(x, f)
    adamGradientDescent(x, f)
    
    batch = BatchGradientDescent()
    batch.descent(x, f)
    momentum = MomentumGradientDescent()
    momentum.descent(x, f)
    print("")
    print(batch.points[-1])
    print(momentum.points[-1])