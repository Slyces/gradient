#!/usr/bin/env python3
# --------------------------------- imports ---------------------------------- #
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import utils, textwrap
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter, AutoLocator
from mpl_toolkits.mplot3d import Axes3D
from getData import getDataFromShortRawData
from functions import Function
from os.path import join
import analyse
# ---------------------------------------------------------------------------- #
directory = 'short_data'

def function_graph(f_name):
    data = getDataFromShortRawData(join(directory, f_name))
    function = Function.functions[f_name]
    def_space = function.def_space
    assert len(def_space) == 2
    # ---------------------- create the figure and axes ---------------------- #
    fig, ax = plt.subplots()

    # -- discretize the definition space and compute the function's images --- #
    X, Y = 
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

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("function")
    args = parser.parse_args()
    print(args.function)

    function_graph(args.function)
