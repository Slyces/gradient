#!/usr/bin/env python3
# --------------------------------- imports ---------------------------------- #
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse, textwrap
from display import display
from algorithms import *
import utils, functions


np.set_printoptions(precision=2)

# list of implemented functions
functions = functions.Function.functions

# @TODO: homogénéiser les noms de variables --> someVar plutôt que some_var

# @TODO: à généraliser avec plusieurs méthodes
def starting_point(def_space: np.array):
    return [np.random.uniform(d[0], d[1], 1)[0] for d in def_space]



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

    parser.add_argument("-r", "--random", action="store_true", dest="random",
            help="Chooses a random starting point")

    # --------------------- extraction of the arguments ---------------------- #
    args = parser.parse_args()

    # tests on args
    assert args.function in functions.keys(), "choose a function from the list"

    function = functions[args.function]
    def_space = function.def_space
    utils.verbose = args.verbose
    gradient_descent = globals()[args.variant + "GradientDescent"]

    # ---------------------- gradient descent algorithm ---------------------- #
    x_0 = starting_point(def_space) if args.random else function.default_start
    data = gradient_descent(x_0, function)
    x_n = data[-1]

   # -----------------------------------  ------------------------------------ #
    print("Gradient descent converged in {n} step from {x_0} ({fx_0}) to {x_n} ({fx_n})".format(
            n= len(data), x_0= x_0, x_n= x_n, fx_0= function(*x_0), fx_n= function(*x_n)))

    # ----------------- displaying the function to optimize ------------------ #
    if not args.no_display:
        display(function, def_space, data, 100)

