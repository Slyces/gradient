import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import utils, textwrap
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter, AutoLocator
from mpl_toolkits.mplot3d import Axes3D

# --------------------- discretize the definition space ---------------------- #
def discretise_space(def_space, n = 100):
    """
    Discretise an n-dimensional space with equally spaced points.
        see np.meshgrid
    """
    dim = len(def_space)
    one_dim_axis = [] # list of coordinates on 1 dim axis
                      # ex : [ x, y ]
                      # x = [0, 0.1, .., 0.9, 1]
                      # y = [2, 2.1, .., 2.9, 3]
    for i in range(dim):
        start, stop = def_space[i]
        one_dim_axis.append(np.linspace(start, stop, n))
    return np.meshgrid(*one_dim_axis)


# --------- compute the function's values over the discretized space --------- #
def compute_over_grid(function, n, *grid):
    # assume equally long mesh of length n
    dim = len(grid)
    results = np.empty([n for i in range(dim)])
    indexes = [0 for i in range(dim)]
    for (idx, _) in np.ndenumerate(grid[0]):
        v = [g[idx] for g in grid]
        results[idx] = function(*v)
    return results

# --------------- plot a 1 dimensional function in a 2D graph ---------------- #
def plot2d(function, def_space, datas, n=40, steps=False):
    """ Plots a one dimensional function on a 2 dimensional graph """
    assert len(def_space) == 1
    # ---------------------- create the figure and axes ---------------------- #
    fig, ax = plt.subplots()

    # -- discretise the definition space and compute the function's images --- #
    x, = discretise_space(def_space, n)
    y = compute_over_grid(function, n, x)

    ax.plot(x, y, '#9A9A9A')

    # ----------------------- all starts are identical ----------------------- #
    start = datas[list(datas.keys())[0]][0]
    ax.scatter(start, function(*start), label='start')


    # ------------------- plot the descent and end points -------------------- #
    colors = iter(cm.rainbow(np.linspace(0, 1, len(datas))))
    for name, data in datas.items():
        color = next(colors)
        end = data[-1]
        ax.plot(data, [function(*v) for v in data], linewidth=1, color=color,
                label=name)
        ax.scatter(end, function(*end), color=color)
        if steps:
            st = ax.scatter(data, [function(*v) for v in data], color=color,
                    s=12)

    # ---------------------------- titles & misc ----------------------------- #
    ax.set_ylim(min(y) - 0.5, max(y) + 0.5)
    ax.set(xlabel='${}$'.format(str(function)),
            title='{} function'.format(type(function).__name__))
    ax.grid()

    ax.legend(loc='best')
    plt.show()

# -------------- plot a 2 dimensional function in a 3D diagram --------------- #
def plot3d(function, def_space, datas, n=40, steps=False):
    """ Plots a two dimensional function on a 3 dimensional graph """
    assert len(def_space) == 2
    # ---------------------- create the figure and axes ---------------------- #
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # -- discretize the definition space and compute the function's images --- #
    X, Y = discretise_space(def_space, n=n)
    Z = compute_over_grid(function, n, X, Y)

    # ----------------------- all starts are identical ----------------------- #
    (start_x, start_y) = datas[list(datas.keys())[0]][0]
    ax.scatter(start_x, start_y, function(start_x, start_y), label='start')

    # ------------------- plot the descent and end points -------------------- #
    colors = iter(cm.rainbow(np.linspace(0, 1, len(datas))))

    # ------------ plots distinctly start and stop of the descent ------------ #
    for name, data in datas.items():
        color = next(colors)
        (stop_x, stop_y) = data[-1]
        ax.scatter(stop_x, stop_y, function(stop_x, stop_y), color=color)
        ax.plot(data[:,0], data[:,1], [function(*v) for v in data], color=color,
                label=name)
        if steps:
            st = ax.scatter(data[:,0], data[:,1], [function(*v) for v in data],
                    color=color, s=12)

    # ----------------------- appearance and plotting ------------------------ #
    ax.set_zlim(np.min(Z) - 0.5, np.max(Z) + 0.5)
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set(ylabel='${}$'.format(str(function)),
            title='{} function'.format(type(function).__name__))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap='binary', alpha=0.5,
               linewidth=0, antialiased=False, zorder=1)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.legend(loc='best')
    plt.show()

# ---------- displays a 2 dimensional functions with levels curves ----------- #
def plotLevels(function, def_space, datas, n=40, steps=False):
    assert len(def_space) == 2
    # ---------------------- create the figure and axes ---------------------- #
    fig, ax = plt.subplots()

    # -- discretize the definition space and compute the function's images --- #
    X, Y = discretise_space(def_space, n=n)
    Z = compute_over_grid(function, n, X, Y)

    cs = ax.contourf(X, Y, Z, locator=AutoLocator(), cmap=cm.PuBu_r)
    # cs = ax.contour(X, Y, Z)

    # ----------------------- all starts are identical ----------------------- #
    start = datas[list(datas.keys())[0]][0]
    ax.scatter(*start, label='start')

    # ------------------- plot the descent and end points -------------------- #
    colors = iter(cm.rainbow(np.linspace(0, 1, len(datas))))

    # ------------ plots distinctly start and stop of the descent ------------ #
    for name, data in datas.items():
        color = next(colors)
        end = data[-1]
        e = ax.scatter(*end, color=color)
        d = ax.plot([x for (x,y) in data], [y for (x,y) in data], linewidth=1,
                label=name, color=color)
        if steps:
            st = ax.scatter(data[:,0], data[:,1], color=color, s=12)

    # ---------------------------- titles & misc ----------------------------- #
    cbar = fig.colorbar(cs) # bar with scales

    ax.set(xlabel='${}$'.format(str(function)),
            title='{} function'.format(type(function).__name__))
    plt.legend(loc='best')
    plt.show()

# ------------------ display any N > 2 dimensional function ------------------ #
def plotNd(function, def_space, data, n=40, steps=False):
    print("The N > 2 dimensional functions are not displayable yet.")

# ----------- "switch case" to handle the display of any function ------------ #
def display(function, def_space, data, n=40, levels=None, steps=False):
    dim = len(def_space)
    if dim == 1:
        utils.vprint("One dimensional function")
        return plot2d(function, def_space, data, n, steps=steps)
    elif dim == 2:
        utils.vprint("Two dimensional function")
        if levels:
            return plotLevels(function, def_space, data, n, steps=steps)
        else:
            return plot3d(function, def_space, data, n, steps=steps)
    else:
        utils.vprint("Three (or more) dimensional function")
        return plotNd(function, def_space, data, n, steps=steps)

# ------------------------------- text display ------------------------------- #
def color(x): # small code to color an output in the terminal
    c = "\033[94m" # color$
    e = "\033[0m" # endline$
    return c + x + e

def text_display(function, datas):
    # example output:
    # + --------- + ----- + ---- + ------- + ----- + --- +
    # | algorithm | start | stop | f(stop) | steps | min |
    # + --------- + ----- + ---- + ------- + ----- + --- +
    # | batch     | 0     | -5   |         |       | yes |
    # + --------- + ----- + ---- + ------- + ----- + --- +
    # | adagrad   | 0     | -5   |         |       |     |
    # + --------- + ----- + ---- + ------- + ----- + --- +
    ordered_columns = ['names', 'starts', 'stops', 'f_stops', 'steps']
    columns = {
            'names' : ['algorithms'] + list(datas.keys()),
            'starts' : ['start'] + [str(data[0])[1:-1] for data in datas.values()],
            'stops' : ['stops'] + [str(data[-1])[1:-1] for data in datas.values()],
            'f_stops' : ['f(stop)'] + [str(function(*data[-1]))
                for data in datas.values()],
            'steps' : ['steps'] + [str(len(data)) for data in datas.values()],
    }
    indent = '   '
    maxs = {key : max(map(len, items)) \
            for (key, items)  in columns.items()}
    sep = indent + '+ ' + ' + '.join(['-' * maxs[c] for c in ordered_columns]) \
            + ' +\n' \
    # ------------------------------------------------------------------------ #
    # color the best algorithm
    indexes = list(range(len(datas)))
    values = list(datas.values())
    best_row = min(indexes, key=lambda i: function(*values[i][-1]))
    # ------------------------------------------------------------------------ #
    rows = ['' for i in range(len(datas) + 1)]
    for i in range(len(datas) + 1):
        rows[i] = indent + '| '
        rows[i] += ' | '.join(columns[c][i].ljust(maxs[c]) \
                for c in ordered_columns)
        rows[i] += ' |\n'
    rows[best_row + 1] = color(rows[best_row + 1])
    return sep + sep.join(rows) + sep[:-1] # strip the final \n

