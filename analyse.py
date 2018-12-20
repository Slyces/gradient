#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils import isFar, isClose
"""
Created on Tue Dec 18 15:41:48 2018

@author: 3415104
"""
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import os


from algorithms import *
from utils import *
from getData import getDataFromShortRawData


def bestGradient(gradient_dictionnary, threshold=1e-02, epsilon=1e-02):
    best_gradient = None
    best_gradient_information = {}
    for gradient, values in gradient_dictionnary.items():
        # If the gradient test is the first one
        if best_gradient is None:
            best_gradient = gradient
            best_gradient_information = values

        # If the gradient test is better
        elif better_descent(values["valeur_optimale"], values["nb_iteration"],best_gradient_information["valeur_optimale"], best_gradient_information["nb_iteration"]):
            best_gradient = gradient
            best_gradient_information = values

    return best_gradient, best_gradient_information

def bestGradientForPoint(list_descents, threshold=1e-02, epsilon=1e-02):
    nb_gradient_is_best = {gradient_name:0 for gradient_name in list_descents[0].keys()}
    for gradient_dictionnary in list_descents:
        nb_gradient_is_best[bestGradient(gradient_dictionnary, threshold, epsilon)[0]]+=1
    return nb_gradient_is_best

def dis(list_points, list_descents, threshold=1e-02, epsilon=1e-02):
    points_best_gradient = {gradient_name:[]  for gradient_name in list_descents[0].keys()}
    for i in range(len(list_descents)):
        points_best_gradient[bestGradient(list_descents[i], threshold, epsilon)[0]]+=[list_points[i]]
    colors = iter(cm.rainbow(np.linspace(0, 1, len(implemented))))
    for i in range(len(implemented)):
        color = next(colors)
        plt.scatter([v[0] for v in points_best_gradient[implemented[i]]], [v[1] for v in points_best_gradient[implemented[i]]], c=color)
    plt.show()

def best(directory):
    keywithmaxval = lambda x: max(list(x), key= lambda x: x[1])[0]
    if not os.path.exists(directory):
        print("Directory doesn't exist")
        return
    gradient_function = {}
    gradients = "adadelta momentum batch nesterov adagrad adam rmsprop".split()
    print(" &" + " & ".join(gradients) + r"\\")
    for function in os.listdir(directory):
        # Si il s'agit bien d'un dossier
        function_directory = os.path.join(directory, function)

        if os.path.isdir(function_directory):
            g = getDataFromShortRawData(function_directory)

            if g[1]:
                best_gradient = bestGradientForPoint(g[1])
                sum_p = sum(map(lambda x: x[1], best_gradient.items()))
                print(" & ".join([function] + [("{:.2%}".format(best_gradient[key] / sum_p)) for key in gradients]) + r"\\")
                gradient_function[function] = keywithmaxval(best_gradient)

    return gradient_function

if __name__ == '__main__':
    dirname = 'all_data'
    best(dirname)
