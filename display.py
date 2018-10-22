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

# ------------------------- plot the function in 2D -------------------------- #
def plot2d():
    """ """

def_space = [[-5, 5], [-5, 5]]
def f(x, y):
    return np.sin(np.sqrt(x * x + y * y))

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
