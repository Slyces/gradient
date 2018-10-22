#!/usr/bin/env python3
# --------------------------------- imports ---------------------------------- #
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse, textwrap
from display import display

np.set_printoptions(precision=2)

# list of implemented functions
functions = ['square', 'sin2d']

# @TODO: homogénéiser les noms de variables --> someVar plutôt que some_var

# ----------------------------- utils functions ------------------------------ #
def vprint(*args, v: int=1):
    if verbose >= v:
        print(*args)

# @TODO: à généraliser avec plusieurs méthodes
def starting_point(def_space: np.array):
    return [np.random.uniform(d[0], d[1], 1)[0] for d in def_space]


# ---------------------- functions and their gradients ----------------------- #
# @TODO: mettre les fonctions dans un fichier séparé
#        utiliser des classes (?)
#
# each function <name> must implement:
#
# f_name(x):           the actual function. Assuming input of correct size.
#
# grad_name(x):    gradient of the function, returns same size as input
#
# 1D functions :
#   def_space_name:    variable containing [[x_min, x_max]] 
#
# 2D functions :
#   def_space_name:    variable containing [[x_min, x_max],

# some derivatives reminders
# (f ∘ g)'(x) = (f' ∘ g)(x) + (f ∘ g')(x)
# sin'(x) = cos(x)

# Square function (x + 5)²
def_space_square = [[-10, 0]]

def f_square(x):
    return (x + 5) * (x + 5)

def grad_square(x):
    return 2 * x + 10

# sin2d sin(x² + y²)
def_space_sin2d = [[-5, 5], [-5, 5]]
def f_sin2d(x, y):
    return np.sin(np.sqrt(x * x + y * y))

def grad_sin2d(x, y):
    sq = np.sqrt(x * x + y * y)
    return np.array(
                np.cos(sq) - np.sin(x / sq),
                np.cos(sq) - np.sin(y / sq)
            )

# ----------------------- gradient descent algorithms ------------------------ #
# @TODO: mettre ces méthodes dans un fichier séparé

# Batch gradient descent
def batchGradientDescent(x_0, func, learningRate=0.01, maxIter=1000):
    """ The gradient descent classic algorithm """
    # constantes
    h = 0.0001 # Variation nécéssaire au calcul du gradient
    dim = len(x_0)
    currentX = np.array(x_0)

    vprint("Starting position :", currentX)

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
            vprint("Itération {} : {}".format(i, currentX ))
    return np.array(listeX)


# ---------------------------- arguments parsing ----------------------------- #
if __name__ == '__main__':
    # ------------------------- program description -------------------------- #
    default = " [default: %(default)s]"
    parser = argparse.ArgumentParser(prog='gradient',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                Gradient descent algorithms comparison
                --------------------------------------
                    This programs is a sandbox made to explore the
                    different gradient descent algorithms and variants
                '''))

    # ------------------------- optionnal parameters ------------------------- #
    parser.add_argument("--variant", metavar="variant", dest='variant', type=str,
                default='batch',
    help="choose the variant among {batch, mini-batch, stochastic}" + default)


    parser.add_argument("-f", metavar="function", dest='function', type=str, default='square',
    help="""choose the function to optimize among {} {}""".format(
        '{' + ', '.join(functions) + '}', default))

    # --------------------------- optionnal flags ---------------------------- #
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                help="incremental verbosity, can be repeated", dest="verbose")

    parser.add_argument("--no-display", action="store_true", dest="no_display")
    args = parser.parse_args()

    gradient = globals()["grad_" + args.function]
    function = globals()["f_" + args.function]
    def_space = globals()["def_space_" + args.function]
    verbose = args.verbose
    gradient_descent = globals()[args.variant + "GradientDescent"]

    # ---------------------- gradient descent algorithm ---------------------- #
    x_0 = starting_point(def_space)
    data = gradient_descent(x_0, function)
    x_n = data[-1]

   # -----------------------------------  ------------------------------------ #
    print("Gradient descent converged in {n} step from {x_0} ({fx_0}) to {x_n} ({fx_n})".format(
            n= len(data), x_0= x_0, x_n= x_n, fx_0= function(*x_0), fx_n= function(*x_n)))

    # ----------------- displaying the function to optimize ------------------ #
    if not args.no_display:
        # @TODO: séparer les fonctions d'affichage dans un fichier, et les
        #        généraliser
        display(function, def_space, data, 100, name=args.function)

