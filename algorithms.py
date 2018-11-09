import numpy as np
import utils

# --------------- descent object wrapping stats of the descent --------------- #
class Descent(object):

    """Wrapper class containing statistics about the descent"""
    def __init__(self):
        """Void init, the descent must be completed sequentially"""
        self.points = np.array([]) # record every points of the descent
        self.gradients = np.array([]) # record every gradient

    # ----------- getters for first and last point of the descent ------------ #
    @property
    def start(self):
        return self.points[0]

    @property
    def stop(self):
        return self.points[0]

    # --------------------- gradually adding statistics ---------------------- #
    def add_point(self, p):
        # TODO: finish this
        pass
# ----------------------- gradient descent algorithms ------------------------ #
implemented = ['batch', 'momentum', 'nesterov', 'adagrad', 'adadelta', 'RMSprop']
h = 10e-4 # Variation nécéssaire au calcul du gradient
epsilon = 5 * 10e-5

# -------------------------- Batch gradient descent -------------------------- #
def batchGradientDescent(x_0, function, learningRate=0.01, maxIter=10e4, **kwargs):
    """ The gradient descent classic algorithm """
    # constantes
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]

    # Initialisation de la variation à v > ϵ
    variation = epsilon * 10e3

    i = 0
    while i < maxIter and np.linalg.norm(variation) >= epsilon:
        variation = function.gradient(currentX, h) * learningRate
        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        i += 1
    return np.array(listeX)

# ------------------------ Momentum gradient descent ------------------------- #
def momentumGradientDescent(x_0, function, gamma=0.9, learningRate=0.01,
        maxIter=10e4, **kwargs):
    # constantes
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]
    listeVariation = [np.array([0 for i in range(dim)])]

    # Initialisation de la variation à v > ϵ
    variation = epsilon * 10e3

    i = 0
    while i < maxIter and np.linalg.norm(variation) >= epsilon:
        variation = function.gradient(currentX, h) * learningRate + \
                gamma * listeVariation[i]
        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
        listeVariation.append(np.copy(variation))

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        i += 1
    return np.array(listeX)

# ------------------------ Nesterov gradient descent ------------------------- #
def nesterovGradientDescent(x_0, function, gamma=0.9, learningRate=0.01,
        maxIter=10e4, **kwargs):
    # constantes
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]
    listeVariation = [np.array([0 for i in range(dim)])]

    # Initialisation de la variation à v > ϵ
    variation = epsilon * 10e3

    i = 0
    while i < maxIter and np.linalg.norm(variation) >= epsilon:
        gammaVar = gamma * listeVariation[i]
        variation = function.gradient(currentX - gammaVar, h) * learningRate \
                + gammaVar
        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
        listeVariation.append(np.copy(variation))

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        i += 1
    return np.array(listeX)


# ------------------------- Adagrad gradient descent ------------------------- #
def adagradGradientDescent(x_0, function, learningRate=0.01, maxIter=10e4, **kwargs):
    # constantes
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX)]

    # Initiliasation de Gt (somme des carrées des gradients trouvés
    # jusqu'à lors pour chaque paramètre)
    squareGradient = np.array([0e-8 for i in range(dim)])

    # Initialisation de la variation à v > ϵ
    variation = epsilon * 10e3

    i = 0
    while i < maxIter and np.linalg.norm(variation) >= epsilon:
        gradient = function.gradient(currentX, h)
        squareGradient += gradient ** 2
        variation = (gradient/ np.sqrt(squareGradient))*learningRate

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        i += 1

    return np.array(listeX)

# ------------------------ Adadelta gradient descent ------------------------- #
def adadeltaGradientDescent(x_0, function, gamma=0.9, maxIter=10e4, **kwargs):
    # constantes
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX), np.copy(currentX)]

    # Initialisation de E[g] et E[O]
    squareGradient = np.array([0 for i in range(dim)])
    squareParameterVariation = np.array([1e-3 for i in range(dim)])

    # Initialisation de la variation à v > ϵ
    variation = epsilon * 10e3

    i = 0
    while i < maxIter - 1 and np.linalg.norm(variation) >= epsilon:
        gradient = function.gradient(currentX, h)

        squareGradient = gamma * squareGradient + \
                (1 - gamma) * (gradient ** 2)
        squareParameterVariation = gamma * squareParameterVariation + \
                (1-gamma) * ((listeX[-1] - listeX[-2]) ** 2)

        variation = np.sqrt(squareParameterVariation) / np.sqrt(squareGradient) \
                * gradient

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire


        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        i += 1

    return np.array(listeX)

# ------------------------- RMSprop gradient descent ------------------------- #
def RMSpropGradientDescent(x_0, function, gamma=0.9, learningRate=0.01,
        maxIter=10e4, **kwargs):
    # constantes
    dim = len(x_0)
    currentX = np.array(x_0, dtype=np.float64)
    smallValues = np.array([1e-8 for i in range(dim)])

    utils.vprint("Starting position :", currentX)

    # Initialisation de la liste des valeurs trouvées
    listeX = [np.copy(currentX), np.copy(currentX)]

    # Initialisation de E[g]
    squareGradient = np.array([0 for i in range(dim)])

    # Initialisation de la variation à v > ϵ
    variation = epsilon * 10e3

    i = 0
    while i < maxIter - 1 and np.linalg.norm(variation) >= epsilon:
        gradient = function.gradient(currentX, h)

        squareGradient = gamma * squareGradient + (1 - gamma) * (gradient ** 2)

        variation = (gradient * learningRate) / \
                np.sqrt(squareGradient + smallValues)

        currentX -= variation # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
        i += 1
    return np.array(listeX)
