#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse, textwrap

# list of implemented functions
functions = ['square', 'sin2d']

# ----------------------------- utils functions ------------------------------ #
def vprint(*args, v = 1):
    if verbose >= v:
        print(*args)

def starting_point(def_space):
    return [np.random.uniform(d[0], d[1], 1)[0] for d in def_space]


# ---------------------- functions and their gradients ----------------------- #
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
def gradient_descent(x_0, f, grad):
    values = [np.array(x_0)]
    rate = 0.1
    epsilon = 0.00001
    max_iter = 10000
    i = 0
    stop = False

    while not stop:
        prev_x = values[-1]
        cur_x = prev_x - rate * gradient(*prev_x)
        values.append(cur_x)
        stop = i >= max_iter or np.linalg.norm(values[-1] - values[-2]) < epsilon
        i += 1
    return values


# ---------------------------- arguments parsing ----------------------------- #
if __name__ == '__main__':
    default = '[default: %(default)s]' # message for default values
    parser = argparse.ArgumentParser(prog='gradient',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                Gradient descent algorithms comparison
                --------------------------------------
                    This programs is a sandbox made to explore the
                    different gradient descent algorithms and variants
                '''))
    parser.add_argument("--variant", metavar="variant", type=str, dest='variant', default='mini-batch',
                help="""choose the variant among {batch, stochastic, mini-batch}
                     """ + default
            )
    parser.add_argument("-f", metavar="function", dest='function', type=str, default='square',
                help="""choose the function to optimize among {}
                        {}""".format('{' + ', '.join(functions) + '}', default)
            )
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                help="incremental verbosity, can be repeated",
                dest="verbose"
            )
    parser.add_argument("--no-display", action="store_true", dest="no_display")
    args = parser.parse_args()

    gradient = globals()["grad_" + args.function]
    function = globals()["f_" + args.function]
    def_space = globals()["def_space_" + args.function]
    verbose = args.verbose
    descent = gradient_descent

    # ---------------------- gradient descent algorithm ---------------------- #
    x_0 = starting_point(def_space)
    values = gradient_descent(x_0, function, gradient)
    np.set_printoptions(precision=2)
    print("Gradient descent converged in {n} step from {x0} ({y0}) to {x} ({y})".format(
            n= len(values), x0= values[0], x= values[-1], y0= function(*x_0), y= function(*values[-1])
        ))

    # ----------------- displaying the function to optimize ------------------ #
    if not args.no_display:
        if len(def_space) == 1:
            # one dimensional case
            vprint("One dimensional function")
            x = np.linspace(*def_space[0], num=100)
            y = [function(x_i) for x_i in x]

            fig, ax = plt.subplots()
            ax.plot(x, y)

            # plot the starting x_0
            ax.scatter(x_0, function(*x_0))
            ax.plot(values, [function(v) for v in values], '-o', markersize=1, linewidth=1)

            ax.set(xlabel='x', ylabel='$y = {}(x)$'.format(args.function),
                    title='{} function'.format(args.function))
            ax.grid()

            plt.show()
        elif len(def_space) == 2:
            vprint("Two dimensional function")

            from matplotlib import cm
            from matplotlib.ticker import LinearLocator, FormatStrFormatter
            from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

            fig = plt.figure()
            ax = fig.gca(projection='3d')

            x = np.linspace(*def_space[0], num=40)
            y = np.linspace(*def_space[1], num=40)
            X, Y = np.meshgrid(x, y)
            Z = np.array([[function(X[i][j], Y[i][j]) for i in range(len(x))]
                                                for j in range(len(y))])

            # Plot the start
            ax.scatter(x_0[0], x_0[1], function(*x_0), 'or', zorder=3)
            print(x_0[0], x_0[1], function(*x_0))

            # Plot the convergence
            values = np.array(values)
            x, y = values[:,0], values[:,1]
            z = np.array([function(x[i],y[i]) for i in range(len(x))])
            ax.plot(x, y, z, label='gradient convergence', linewidth=2, zorder=2)

            # Customize the z axis.
            ax.set_zlim(-1.01, 1.01)
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

            # Plot the surface.
            surf = ax.plot_surface(X, Y, Z, cmap='binary', alpha=0.5, # cm.coolwarm,
                       linewidth=0, antialiased=False, zorder=1)

            # Add a color bar which maps values to colors.
            fig.colorbar(surf, shrink=0.5, aspect=5)

            plt.show()

