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
# @TODO: mettre ces méthodes dans un fichier séparé

# Batch gradient descent
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
        gradient = np.array([])
        # Calcul du gradient pour chaque dimension
        for j in range(dim):
            # @TODO: mieux commenter
            # Création de la variation : [0 .. h .. 0] (valeur h en position k)
            liste = np.array([0 if k != j else h for k in range(dim)])
            gradJ = (function(*(currentX + liste)) - function(*currentX)) / h
            gradient = np.append(gradient, [learningRate * gradJ])

        currentX -= gradient # Modification de X
        listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

        if i % 500 == 0:
            utils.vprint("Itération {} : {}".format(i, currentX ))
    return np.array(listeX)

