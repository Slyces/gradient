#!/usr/bin/env python3
# --------------------------------- imports ---------------------------------- #
import numpy as np, matplotlib, matplotlib.pyplot as plt, argparse, textwrap, re
from display import display, text_display
from algorithms import *
import utils, functions

# @TODO: ajouter des prints quand on force le start dans l'espace de definition
# @TODO: ajouter learning rate en option
# @TODO: ajouter des points intermédiaires
#

np.set_printoptions(precision=2)

# list of implemented functions
functions = functions.Function.functions

# @TODO: homogénéiser les noms de variables --> someVar plutôt que some_var

# @TODO: à généraliser avec plusieurs méthodes
def random_starting_point(def_space: np.array):
    return [np.random.uniform(d[0], d[1], 1)[0] for d in def_space]

# ------------------------------- parser setup ------------------------------- #
def setup_parser():
    # ------------------------- program description -------------------------- #
    default = "[default: %(default)s]"
    parser = argparse.ArgumentParser(prog='gradient',
            formatter_class=argparse.RawTextHelpFormatter,
            description=textwrap.dedent('''\
                Gradient descent algorithms comparison
                --------------------------------------
                    This programs is a sandbox made to explore the
                    different gradient descent algorithms and variants
                '''))

    # ------------------------- optionnal parameters ------------------------- #
    # variants
    parser.add_argument("--variant", metavar="variant", dest='variant', type=str,
                default='batch', choices= ['batch', 'mini-batch', 'stochastic'],
    help=textwrap.dedent("""\
            choose the variant among {batch, mini-batch, stochastic}
            """) + default)


    # algorithms: list of implemented algorithms imported from algorithms.py
    parser.add_argument("-a", "--algorithm", metavar="algo", action='append',
            dest="algorithms", type=str,
            choices=implemented + [str(i) for i in range(len(implemented))],
            help=textwrap.dedent("""\
                    Uses the given algorithm to find a local minima.
                    Repeat the option to compare multiple algorithms.
                    Choose the algorithm amongst:\n
                    {}\n
                    You can provide the algorithm's number instead of its name.
                    If 'all' is supplied, every algorithm will be used.
                    If no algorithm is supplied, default will be [batch]\
                    """).format('\n'.join([str(n) + '. ' + a for n,a in \
                         enumerate(['all'] + implemented)])))

    # functions
    parser.add_argument("-f", "--function", metavar="f", dest='function',
            type=str, default='square', choices=functions,
            help=textwrap.dedent("""\
                    choose the function f to optimize amongst {}
                    {}""".format(
                        '{' + ', '.join(functions) + '}', default)))
    # definition space
    parser.add_argument("-d", "--def-space", metavar="def-sp",
            dest='def_space', type=str, help=textwrap.dedent("""\
                    definition space : [[x₁-min, x₁-max],
                                        [x₂-min, x₂-max],
                                              ...       ,
                                        [x_n-min, x_n-max]] (with n = dim(f))"""))

    # starting point
    parser.add_argument("-s", "--start", metavar="starting-point", dest='start',
            type=str, help=textwrap.dedent("""\
                    Starting point : 'x_1 x_2 .. x_n' (with n = dim(f))"""))

    # --------------------------- optionnal flags ---------------------------- #
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                help="incremental verbosity, can be repeated", dest="verbose")

    parser.add_argument("--no-display", action="store_true", dest="no_display",
            help="do not use graphics outputs")

    parser.add_argument("-r", "--random", action="store_true", dest="random",
            help="Chooses a random starting point")

    parser.add_argument("--levels", action="store_true", dest="levels",
            help="If dim = 2, plots the 2D levels curves instead of a 3D " \
                    "visualisation")

    return parser

# --------------------- test user def space with a regex --------------------- #
def parse_def_space(def_space, args):
    re_min_max = re_float + ' ' + re_float
    re_def_space = r'\[?(\[' + re_min_max + r'\] ?){' + str(dim) + r'}\]?'
    if args.def_space and re.match(re_def_space, args.def_space):
        floats = re.findall(re_float, args.def_space)
        floats = [float(f.replace(',', '.')) for f in floats]
        # the first re to match will be every dim's min_max
        def_space = [[floats[2 * i], floats[2 * i + 1]] for i in range(dim)]
    elif args.def_space:
        print("[arg missmatch] def_space did not match the expected pattern")

    return def_space

# ------------------ test user starting point with a regex ------------------- #
# also replaces the starting point in the def space if it's missplaced
def parse_starting_point(x_0, args):
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
    if not all([min_ < x_0[i] < max_ for i, (min_, max_) in enumerate(def_space)]):
        x_0 = random_starting_point(def_space)
    return x_0

# ---------------------------- arguments parsing ----------------------------- #
if __name__ == '__main__':
    parser = setup_parser()

    # -------------- regular expressions for arguments checking -------------- #
    re_float = r'(-?\d+[\.,]?\d*)'

    # --------------------- extraction of the arguments ---------------------- #
    args = parser.parse_args()

    # function
    function = functions[args.function]
    dim = len(function.def_space)

    # definition space
    def_space = parse_def_space(function.def_space, args)

    # starting point
    x_0 = random_starting_point(def_space) if args.random else function.default_start
    x_0 = parse_starting_point(x_0, args)

    # algorithms
    algorithms = args.algorithms if args.algorithms is not None else ['batch']
    for (i, a) in enumerate(algorithms):
        if a in [str(x) for x in range(len(implemented))]:
            algorithms[i] = (['all'] + implemented)[int(a)]
    if 'all' in algorithms:
        algorithms = implemented

    # assertions on args
    assert args.function in functions.keys(), "choose a function from the list"

    utils.verbose = args.verbose

    # gradient_descent = globals()[args.variant + "GradientDescent"]

    # ---------------------- gradient descent algorithm ---------------------- #
    datas = {}
    for descent_name in algorithms:
        descent = globals()[descent_name + "GradientDescent"]
        datas[descent_name] = descent(x_0, function, maxIter=999)

    # ----------------------- display the text results ----------------------- #
    print(text_display(function, datas))

    # ----------------- displaying the function to optimize ------------------ #
    if not args.no_display:
        display(function, def_space, datas, 100, levels=args.levels)

