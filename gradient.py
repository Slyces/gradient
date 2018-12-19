#!/usr/bin/env python3
# --------------------------------- imports ---------------------------------- #
import numpy as np, matplotlib, matplotlib.pyplot as plt, argparse, textwrap, re
from display import display, text_display
from algorithms import *
from files import *
import utils, functions
import os
#
# TODO: ajouter des points intermédiaires #


np.set_printoptions(precision=2)

# list of implemented functions
functions_list = functions.Function.functions

# @TODO: homogénéiser les noms de variables --> someVar plutôt que some_var

# @TODO: à généraliser avec plusieurs méthodes
def random_starting_point(def_space: np.array):
    return [np.random.uniform(d[0], d[1], 1)[0] for d in def_space]

# ─────────────────────────────────── test ─────────────────────────────────── #

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
    # Variants
    parser.add_argument("--variant", metavar="variant", dest='variant', type=str,
                default='batch', choices= ['batch', 'mini-batch', 'stochastic'],
    help=textwrap.dedent("""\
            choose the variant among {batch, mini-batch, stochastic}
            """) + default)


    # Algorithms: list of implemented algorithms imported from algorithms.py
    valid_choices = ['all'] + implemented
    parser.add_argument("-a", "--algorithm", metavar="algo", action='append',
            dest="algorithms", type=str,
            choices=valid_choices + [str(i) for i in range(len(valid_choices))],
            help=textwrap.dedent("""\
                    Uses the given algorithm to find a local minima.
                    Repeat the option to compare multiple algorithms.
                    Choose the algorithm amongst:\n
                    {}\n
                    You can provide the algorithm's number instead of its name.
                    If 'all' is supplied, every algorithm will be used.
                    If no algorithm is supplied, default will be [batch]\
                    """).format('\n'.join([str(n) + '. ' + a for (n, a) in \
                         enumerate(valid_choices)])))

    # Functions
    parser.add_argument("-f", "--function", metavar="f", dest='function',
            type=str, default='square', choices=functions_list,
            help=textwrap.dedent("""\
                    choose the function f to optimize amongst {}
                    {}""".format(
                        '{' + ', '.join(functions_list) + '}', default)))

    # Definition space
    parser.add_argument("-d", "--def-space", metavar="def-sp",
            dest='def_space', type=str, help=textwrap.dedent("""\
                    definition space : [[x₁-min x₁-max],[x₂-min x₂-max],...,[x_n-min x_n-max]]
                    (with n = dim(f))"""))

    # Starting point
    parser.add_argument("-s", "--start", metavar="starting-point", dest='start',
            type=str, help=textwrap.dedent("""\
                    Starting point : 'x_1 x_2 .. x_n' (with n = dim(f))
                    Please specify a starting point included in the definition
                    space.
                    In case of invalidity, falls back to default.
                    In case od default's invalidity, falls back to random."""))

    # Learning rate
    parser.add_argument("-l", "--LR", metavar="learning-rate", dest="lrate",
            type=float, help="Learning rate of the descent algorithms. Default=0.01", default=1e-2)

    # Gamma
    parser.add_argument("-gamma", "--gamma", metavar="gamma", dest="gamma",
            type=float, help="Gamma of the descent algorithms. Default=0.8", default=0.8)

    # Beta 1
    parser.add_argument("-beta1", "--beta1", metavar="beta1", dest="beta1",
            type=float, help="Beta 1 of the descent algorithms. Default=0.9", default=0.9)

    # Beta 2
    parser.add_argument("-beta2", "--beta2", metavar="beta2", dest="beta2",
            type=float, help="Beta 2 of the descent algorithms. Default=0.999", default=0.999)

    # Iteration number
    parser.add_argument("--iter", metavar="iter", dest='iter', type=int, default=10000,
    help=textwrap.dedent("""\
            Choose how many iteration the descent will do without converging}
            """) + default)

    # Maximum duration
    parser.add_argument("--maxtime", metavar="maxtime", dest='maxtime', type=int, default=1e8,
    help=textwrap.dedent("""\
            Choose how many time (seconds) the descent will do without converging}
            """) + default)

    # Save data
    parser.add_argument("--save-data", dest='data_path',
    default="",
    help=textwrap.dedent("""\
            file which contain every data of the gradient descent}
            """))

    # Save summary
    parser.add_argument("--save-summary", dest='summary_path',
    default="",
    help=textwrap.dedent("""\
            file which contain a sum up of the gradient descent}
            """))

    # Save parameters
    parser.add_argument("--save-parameters", dest='parameters_path',
    default="",
    help=textwrap.dedent("""\
            file which contain the parameter need to restart the test}
            """))

    # Save everything to a directory
    parser.add_argument("--create-directory", dest='directory_path',
    default="",
    help=textwrap.dedent("""\
            path to create a diretory containing parameters, raw data and a summary
            """))

    # --------------------------- optionnal flags ---------------------------- #
    # Verbosity (display more or less debug informations)
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                help="incremental verbosity, can be repeated", dest="verbose")

    # Turn on & off graphical interface
    parser.add_argument("--no-display", action="store_true", dest="no_display",
            help="do not use graphics outputs")

    # Select starting point at random
    parser.add_argument("-r", "--random", action="store_true", dest="random",
            help="Chooses a random starting point. Overrides -s (manual starting point)")

    # Turn on level plotting
    parser.add_argument("--levels", action="store_true", dest="levels",
            help="If dim = 2, plots the 2D levels curves instead of a 3D " \
                    "visualisation")

    # Show steps of the descent
    parser.add_argument("--steps", action="store_true", dest="steps",
            help="Show the steps of the decent (points on the path).")

    return parser

# --------------------- test user def space with a regex --------------------- #
def parse_def_space(def_space, args):
    re_min_max = re_float + '[ ,] ?' + re_float
    re_def_space = r'\[?(\[' + re_min_max + r'\][ ,]?){' + str(dim) + r'}\]?'
    if args.def_space and re.match(re_def_space, args.def_space):
        floats = re.findall(re_float, args.def_space)
        floats = [float(f.replace(',', '.')) for f in floats]
        # the first re to match will be every dim's min_max
        def_space = [[floats[2 * i], floats[2 * i + 1]] for i in range(dim)]
    elif args.def_space:
        print("[arg missmatch] def_space did not match the expected pattern")

    return def_space

# ------------------ test user starting point with a regex ------------------- #
# also replaces the starting point in the def space if it's missplaced
# Expected behaviour :
#   if 'random' flag is on, return a random point
#   if 'start' is provided and valid, return it
#   else if start is not valid / not provided, fall back to default
#   if defaut is not valid, fall back to random
def parse_starting_point(x_default, args):
    re_x0 = re_float + r'( ' + re_float + r'){' + str(dim - 1) + r'}'
    if args.start and re.match(re_x0, args.start):
        floats = re.findall(re_float, args.start)
        x_ = [float(f.replace(',', '.')) for f in floats]
        if all([min_ <= x_[i] <= max_ for i, (min_, max_)
            in enumerate(def_space)]):
            return x_
        else:
            print("[arg missmatch] start-position is correct, but not in def" \
                  "space. Falling back to default.")
    elif args.start:
        print("[arg missmatch] start-position did not match the expected" \
              "pattern. Falling back to default.")
    if not all([x_min <= x <= x_max for (x, (x_min, x_max))\
            in zip(x_default, def_space)]):
        print("[arg missmatch] default start-position is not in def space. " \
              "Falling back to random.")
        return random_starting_point(def_space)
    return x_default

# ---------------------------- arguments parsing ----------------------------- #
if __name__ == '__main__':
    parser = setup_parser()
    # @TODO: Utiliser les gradients objets plutôt que fonction

    # -------------- regular expressions for arguments checking -------------- #
    re_float = r'(-?\d+[\.,]?\d*)'

    # --------------------- extraction of the arguments ---------------------- #
    args = parser.parse_args()

    # function
    function = functions_list[args.function]
    dim = len(function.def_space)

    # definition space
    def_space = parse_def_space(function.def_space, args)

    # starting point
    if args.random :
        x_0 = random_starting_point(def_space)
    else:
        x_0 = parse_starting_point(function.default_start, args)

    # algorithms
    algorithms = args.algorithms if args.algorithms is not None else ['batch']
    for (i, alg) in enumerate(algorithms):
        if alg in [str(x) for x in range(len(implemented))]:
            algorithms[i] = (['all'] + implemented)[int(alg)]
    if 'all' in algorithms:
        algorithms = implemented

    # Modification of algorithms name in order to match with their class
    algorithms = [algo[0].upper()+algo[1:] for algo in algorithms]

    # assertions on args
    assert args.function in functions_list.keys(), "choose a function from the list"

    utils.verbose = args.verbose


    # ---------------------- gradient descent algorithm ---------------------- #
    datas = {}
    times = {}
    for descent_name in algorithms:
        gradientClass = globals()[descent_name + "GradientDescent"]
        gradient = gradientClass(learningRate= args.lrate, gamma = args.gamma, beta1=args.beta1, beta2=args.beta2)
        gradient.descent(x_0, function, args.iter,args.maxtime, epsilon)

        datas[descent_name] = np.array(gradient.points)
        times[descent_name] = gradient.tempsDescent
        # -------------------------- writing files --------------------------- #
        if args.directory_path:
            if not os.path.isdir(args.directory_path):
                os.mkdir(args.directory_path)
            args.summary_path = os.path.join(args.directory_path, 'summary')
            args.parameters_path = os.path.join(args.directory_path, 'parameters')
            args.data_path = os.path.join(args.directory_path, 'data')
        if args.summary_path:
            writeSummary(args.summary_path, gradient, function)
        if args.parameters_path:
            writeParameters(args.parameters_path, gradient,
                    (args.lrate, args.gamma, args.beta1, args.beta2),
                    (x_0, function, args.iter, args.maxtime, epsilon))
        if args.data_path:
            writeData(args.data_path, gradient)
        # -------------------------------------------------------------------- #

    # ----------------------- display the text results ----------------------- #
    print(text_display(function, datas, times))

    # ----------------- displaying the function to optimize ------------------ #
    if not args.no_display:
        display(function, def_space, datas, 100, levels=args.levels, steps=args.steps)
