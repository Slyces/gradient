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
    points, descents = getDataFromShortRawData(join(directory, f_name))
    function = Function.functions[f_name]
    def_space = function.def_space
    assert len(def_space) == 2
    # ------------------------------------------------------------------------ #
    points = np.array(points)
    # ---------------------- create the figure and axes ---------------------- #
    fig, ax = plt.subplots()

    gradients_names = list(descents[0].keys())

    best_gradients = [analyse.bestGradient(grad) for grad in descents]

    # ---------------- plot the points and the best gradient ----------------- #
    colors = list(cm.rainbow(np.linspace(0, 1, len(gradients_names))))
    scatters = {}

    for i in range(len(points)):
        p, (grad_name, grad_dict) = points[i], best_gradients[i]
        color = colors[gradients_names.index(grad_name)]
        scatters[grad_name] = ax.scatter(*p, color=color, s=12, alpha=0.8)

    # ---------------------------- titles & misc ----------------------------- #
    ax.set(xlabel='${}$'.format(str(function)),
            title='{} function'.format(type(function).__name__))
    keys = list(scatters.keys())
    plt.legend([scatters[key] for key in keys], keys,
           scatterpoints=1,
           loc='best',
           fontsize=8)
    plt.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("function")
    args = parser.parse_args()

    function_graph(args.function)
