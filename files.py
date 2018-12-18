#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------- imports ---------------------------------- #
from algorithms import *
from display import text_display
# ---------------------------------------------------------------------------- #


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
def writeSummary(file_name, gradient, function):
    with open(file_name, "w") as sum_file:
        sum_file.write(text_display(function,
            {gradient.nom : gradient.points},
            {gradient.nom : gradient.tempsDescent}))
        

def writeShortData(file_name, gradient):
    with open(file_name, "w") as file:
        s = ""
        for v in gradient.points[-1]:
            s += str(v) + " "
        s+="\n"
        file.write(s)
        file.write(str(gradient.valeurs[-1])+"\n")
        file.write(str(gradient.tempsDescent)+"\n")
        file.write(str(gradient.iteration))
        
        
        
        
        
