#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils import isFar, isClose
"""
Created on Tue Dec 18 15:41:48 2018

@author: 3415104
"""
def bestGradient(gradient_dictionnary, threshold=1e-03, epsilon=1e-02):
    best_gradient = None
    best_gradient_information = {}
    for gradient, values in gradient_dictionnary.items():
        # If the gradient test is the first one
        if best_gradient is None:
            best_gradient = gradient
            best_gradient_information = values

        # If the gradient test is better in term of values
        elif isFarLower(values["valeur_optimale"], best_gradient_information["valeur_optimale"], threshold):
            best_gradient = gradient
            best_gradient_information = values

        # If the gradient test is close to the best and the number of iteration is inferior
        elif isClose(values["valeur_optimale"], best_gradient_information["valeur_optimale"], epsilon) and values["nb_iteration"] < best_gradient_information["nb_iteration"]:
            best_gradient = gradient
            best_gradient_information = values

    return best_gradient, best_gradient_information

def bestGradientForPoint(list_descents, threshold=1e-02, epsilon=1e-02):
    print(list_descents)
    p=list_descents[0]
    print(p.keys())
    nb_gradient_is_best = {gradient_name:0 for gradient_name in list_descents[0].keys()}
    for gradient_dictionnary in list_descents:
        nb_gradient_is_best[bestGradient(gradient_dictionnary, threshold, epsilon)[0]]+=1
    return nb_gradient_is_best
