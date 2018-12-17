#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------- imports ---------------------------------- #
from algorithms import *


"""
Import des données
Retourne le gradient associé
"""
def readData(file_name):
    with open(file_name, "r") as data_file:
        gradient = GradientDescent()
        header = data_file.readline()

        line = data_file.readline()
        while line[0] != "P":
            pts, valeur = line.split(";")

            gradient.valeurs.append(float(valeur))
            point = pts.split(" ")
            gradient.points.append(float(point))

            line = data_file.readline()

        line = data_file.readline() # optimal points and value

        line = data_file.readline()
        line = data_file.readline()
        time, iter = line.split(";")
        gradient.tempsDescent = float(time)

    return dic



"""
file_name : path to the file where the data will be saved
gradient : gradient descent algorithm to use
gradient_param : parameters of the gradient
descent_param : parameter of the descent
"""
def writeData(file_name, gradient):
    # point ; value
    # (0,0) ; 0.247
    #      ...
    # (4,1) ; 0.003
    # OptPoint ; OptValue
    # (4.2,2.5); 0.0001
    with open(file_name, "w") as writing_file:
        # writing in the file
        writing_file.write("Point;Valeur\n")

        for i in range(len(gradient.points)):
            s = ""
            pts = gradient.points[i]
            for v in pts:
                s += str(v) + " "
            s = s[:-1]
            s += ";"
            s += str(gradient.valeurs[i])
            s = s[:-3] + "\n"

            writing_file.write(s)

        s = "PointOptimal;ValeurOptimale\n"

        writing_file.write(s)

        s = str(gradient.points[-1]) + ";" + str(gradient.valeurs[-1]) + "\n"
        writing_file.write(s)

        s = "Temps;Nb iteration\n"
        writing_file.write(s)

        s = str(gradient.tempsDescent) + ";" + str(gradient.iteration)
        writing_file.write(s)

"""
file_name : file_name du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
gradient_param : Les parametres du gradient
descent_param : Les parametres de la descent
"""
def writeParameters(file_name, gradient, gradient_param, descent_param):
    with open(file_name, "w") as fichier:
        fichier.write(file_name + "\n")
        fichier.write(str(gradient_param) + "\n")
        fichier.write(str(descent_param) + "\n")

"""
file_name : path to the file where the data will be saved
gradient : name of the gradient descent algorithm will be used
gradient_param : parameters of the gradient
descent_param : parameters of the descent
"""
def writeSummary(file_name, gradient):
    with open(file_name, "w") as fichier:
        # Nom du gradient
        fichier.write(file_name + "\n")
        # Point et valeur optimale
        fichier.write("La descente de gradient c'est arrêtée au point " + str(gradient.points[-1]) + " de valeur " + str(gradient.valeurs[-1]) + "\n")
        # Temps de calcul
        fichier.write("Le temps de calcul est " + str(gradient.tempsDescent) + "\n")
        # Nombre d'itération
        fichier.write("Il y a eu " + str(gradient.iteration) + " iterations\n")
        # Other useful data
