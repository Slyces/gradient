#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ───────────────────────────────── imports ────────────────────────────────── #
import numpy as np, utils, random, matplotlib.pyplot as plt, os
from functions import *
from algorithms import *
from files import *
from time import time






# ──────────────────────────────────────────────────────────────────────────── #

def generateData(nb_points, function_name):

    directory = "generated_data"
    epsilon = 0.001 # la marge d'erreur
    nbPoints = nb_points

    # Pour chaque fonction
    #   Pour chaque point
    #     Pour chaque algorithm
    #       Pour chaque configuration de paramètres

    functions = [globals()[function_name]]
    algorithms = [
            BatchGradientDescent,
            MomentumGradientDescent,
            NesterovGradientDescent,
            AdagradGradientDescent,
            AdadeltaGradientDescent,
            RmspropGradientDescent,
            AdamGradientDescent]

    # Les valeurs des différents paramètre à étudier
    parameters_exploration = {
        'learningRate': [10e-4 + 10e-4 * (i ** 2) for i in range(50)],
        'gamma':  [0.99 - 0.001 * (i ** 2) for i in range(20)],
        'beta1': [0.80, 0.85, 0.9, 0.95, 0.99],
        'beta2': [0.9, 0.95, 0.999, 0.9999]
    }


    for function in functions:
        print("generating function " + function.name)
        function_directory = .os.path.join(directory, function.name)
        if not os.path.exists(function_directory):
            os.makedirs(function_directory)

        points = [[random.uniform(v[0], v[1]) for v in function.def_space]
                for i in range(nbPoints)]

        for point in points:
            str_point = ''.join(str(point).split(' '))
            print("generating point" + str_point)
            point_directory = os.path.join(function_directory, str_point)
            if not os.path.exists(point_directory):
                os.makedirs(point_directory)

            for algorithm in algorithms:
                print("generating algorithm " + algorithm.nom)
                algorithm_directory = os.path.join(point_directory, algorithm.nom)
                if not os.path.exists(algorithm_directory):
                    os.makedirs(algorithm_directory)


                # On regarde si ça vaut la peine d'étudier tout les parametres
                params = {'learningRate': [0], 'gamma': [0], 'beta1': [0], 'beta2': [0]}
                for key in algorithm.params:
                    params[key] = parameters_exploration[key]

                gradient_parameter = {}
                descent_parameter = {}
                bestGradient = None
                # Pour toute les possibilités de paramêtre
                for learningRate in params['learningRate']:
                    for gamma in params['gamma']:
                        for beta1 in params['beta1']:
                            for beta2 in params['beta2']:

                                # Calcul du gradient
                                gradient = algorithm(learningRate=learningRate,
                                        gamma=gamma, beta1=beta1, beta2=beta2)
                                gradient.descent(point, function)

                                # On garde seulement si c'est meilleur
                                # Si il n'y a pas de gradient
                                # Si il converge vers un bien meilleur valeur
                                # Si il converge au même endroit mais qu'il le fait plus vite
                                current_value = gradient.valeurs[-1]
                                if bestGradient is None or\
                                        bestGradient.valeurs[-1] - gradient.valeurs[-1] > epsilon \
                                        or (abs(gradient.valeurs[-1] - bestGradient.valeurs[-1]) < epsilon * 0.1 and gradient.iteration < bestGradient.iteration):
                                    # Préparer les paramêtres pour les conserver
                                    gradient_parameter = {
                                            "learningRate": learningRate,
                                            "gamma": gamma,
                                            "beta1": beta1,
                                            "beta2": beta2
                                            }
                                    descent_parameter = {"x_0":point, "function":function}
                                    bestGradient = gradient

                # Génération des données
                writeData(os.path.join(algorithm_directory, "raw_data.txt"), bestGradient)
                writeParameters(os.path.join(algorithm_directory, "parameters.txt"),
                        bestGradient, gradient_parameter, descent_parameter)
                writeSummary(os.path.join(algorithm_directory, "summary.txt"), bestGradient)

"""
Lancement du programme
"""
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--nb_points', dest='nb_points', type=int, default=10)
    parser.add_argument('--function', dest='function', type=str)

    args = parser.parse_args()

    generateData(args.nb_points, args.function)




