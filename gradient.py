#!/usr/bin/env python3
# --------------------------------- imports ---------------------------------- #
import numpy as np, matplotlib, matplotlib.pyplot as plt, argparse, textwrap, regex as re
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


    parser.add_argument("-f", metavar="function", dest='function', type=str,
            default='square', help="""choose the function to optimize
            among {} {}""".format('{' + ', '.join(functions) + '}', default))

    parser.add_argument("-d", "--def-space", metavar="definition-space",
            dest='def_space', type=str, help=""" definition space :
            [[x₁-min, x₁-max], [x₂-min, x₂-max], ..., [x𝑛-min, x𝑛-max]]
             (with n = dim(f))""")

    parser.add_argument("-s", "--start", metavar="starting-point", dest='start',
            type=str, help="""
            Starting point : 'x_1 x_2 .. x_n' (with n = dim(f))""")

    # --------------------------- optionnal flags ---------------------------- #
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                help="incremental verbosity, can be repeated", dest="verbose")

    parser.add_argument("--no-display", action="store_true", dest="no_display")

    parser.add_argument("-r", "--random", action="store_true", dest="random",
            help="Chooses a random starting point")

    parser.add_argument("--levels", action="store_true", dest="levels",
            help="If dim = 2, plots the 2D levels curves instead of a 3D " \
                    "visualisation")

    # -------------- regular expressions for arguments checking -------------- #
    re_float = r'(-?\d+[\.,]?\d*)'
    re_min_max = re_float + ' ' + re_float

    # --------------------- extraction of the arguments ---------------------- #
    args = parser.parse_args()

    # function
    function = functions[args.function]
    dim = len(function.def_space)

    # definition space
    def_space = function.def_space
    re_def_space = r'\[?(\[' + re_min_max + r'\] ?){' + str(dim) + r'}\]?'
    if args.def_space and re.match(re_def_space, args.def_space):
        floats = re.findall(re_float, args.def_space)
        floats = [float(f.replace(',', '.')) for f in floats]
        # the first re to match will be every dim's min_max
        def_space = [[floats[2 * i], floats[2 * i + 1]] for i in range(dim)]
    elif args.def_space:
        print("[arg missmatch] def_space did not match the expected pattern")

    # starting point
    re_x0 = re_float + r'( ' + re_float + r'){' + str(dim - 1) + r'}'
    if args.start and re.match(re_x0, args.start):
        floats = re.findall(re_float, args.start)
        x_ = [float(f.replace(',', '.')) for f in floats]
        if all([min_ < x_[i] < max_ for i, (min_, max_)
            in enumerate(def_space)]):
            x_0 = x_
        else:
            print("[arg missmatch] start-position is correct, but not in def" \
                  "space")
    elif args.start:
        print("[arg missmatch] start-position did not match the expected" \
              "pattern")
    x_0 = starting_point(def_space) if args.random else function.default_start
    if not all([min_ < x_0[i] < max_ for i, (min_, max_) in enumerate(def_space)]):
        x_0 = starting_point(def_space)


    # assertions on args
    assert args.function in functions.keys(), "choose a function from the list"

    utils.verbose = args.verbose

    gradient_descent = globals()[args.variant + "GradientDescent"]

    # ---------------------- gradient descent algorithm ---------------------- #
    data = gradient_descent(x_0, function)
    x_n = data[-1]

   # -----------------------------------  ------------------------------------ #
    print("Gradient descent converged in {n} step from {x_0} ({fx_0}) to {x_n} ({fx_n})".format(
            n= len(data), x_0= x_0, x_n= x_n, fx_0= function(*x_0), fx_n= function(*x_n)))

    # ----------------- displaying the function to optimize ------------------ #
    if not args.no_display:
        display(function, def_space, data, 100, levels=args.levels)

