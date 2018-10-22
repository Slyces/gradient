import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
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
        results[idx] = f(*v)
    return results

# --------------- plot a 1 dimensional function in a 2D graph ---------------- #
def plot2d(function, def_space, data, n=40):
    """ Plots a one dimensional function on a 2 dimensional graph """
    # ---------------------- create the figure and axes ---------------------- #
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # -- discretize the definition space and compute the function's images --- #
    x, = discretize_space(def_space, n)
    y = compute_over_grid(function, n, x)

    # ----------------- plot the starting and ending points ------------------ #
    start, end = data[0], data[-1]

    ax.scatter(start, function(start), 'r')
    ax.scatter(end, function(end), 'g')
    ax.plot(data, compute_over_grid(function, len(data), data),
        '#CACACA', linewidth=1)

    # ---------------------------- titles & misc ----------------------------- #
    ax.set_ylim(min(y) - 0.5, max(y) + 0.5)
    ax.set(xlabel='x', ylabel='$y = {}(x)$'.format(args.function),
            title='{} function'.format(args.function))
    ax.grid()
    plt.show()

# -------------- plot a 2 dimensional function in a 3D diagram --------------- #
def plot3d(function, def_space, data, n=40):
    """ Plots a two dimensional function on a 3 dimensional graph """
    # ---------------------- create the figure and axes ---------------------- #
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # -- discretize the definition space and compute the function's images --- #
    X, Y = discretise_space(def_space, n=n)
    Z = compute_over_grid(f, n, X, Y)

    # ------------ plots distinctly start and stop of the descent ------------ #
    start, stop = data[0], data[-1]
    ax.scatter(start, function(*start), 'r')
    ax.scatter(stop, function(*stop), 'g')

    # ----------------------- appearance and plotting ------------------------ #
    ax.set_zlim(min(Z) - 0.5, max(Z) + 0.5)
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap='binary', alpha=0.5,
               linewidth=0, antialiased=False, zorder=1)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

# ------------------ display any N > 2 dimensional function ------------------ #
def plotNd(function, def_space, data, n=40):
    print("The N > 2 dimensional functions are not displayable yet.")

# ----------- "switch case" to handle the display of any function ------------ #
def display(function, def_space, data, n=40):
    dim = len(def_space)
    if dim == 1:
        return plot2d(function, def_space, data, n)
    elif dim == 2:
        return plot3d(function, def_space, data, n)
    else:
        return plotNd(function, def_space, data, n)


if __name__ == '__main__':
    # Plot of the function
    N = 40

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X, Y = discretise_space(def_space, n=N)
    Z = compute_over_grid(f, N, X, Y)


    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap='binary', alpha=0.5, # cm.coolwarm,
               linewidth=0, antialiased=False, zorder=1)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
