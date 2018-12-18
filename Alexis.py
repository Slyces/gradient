#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:44:10 2018

@author: 3415104
"""
from functions import *
from gradient import *
from algorithms import *
from random import uniform
import numpy as np

# Pour chaque fonction
# Pour chaque points intéressant dans ces fonctions
# Pour chaque méthode
# Pour chaque ensemble de parametre
# Appliquer la descente

nbPoints = 10 # Nombre de points à tester
fonctions = [sin2d]

learningRate = [1e-5*(i+1)**2 for i in range(100)]
gamma = [0.5 + 0.01*i for i in range(50)]
beta1 = [0.9]
beta2 = [0.999]

for fonction in fonctions:
    # Choix d'un points dans l'espace de définition
    for i in range(nbPoints):
        point = [uniform(defSpace[0], defSpace[1]) for defSpace in fonction.def_space]
        for gradient in [algo[0].upper()+algo[1:] for algo in implemented]:
            gradientClass = globals()[gradient + "GradientDescent"]
            
            
            
            # Pour chaque paramètre
            valeur = []
            if "learningRate" in gradientClass.params:
                valeur.append(learningRate)
            if "gamma" in gradientClass.params:
                valeur.append(gamma)
            if "beta1" in gradientClass.params:
                valeur.append(beta1)
            if "beta2" in gradientClass.params:
                valeur.append(beta2)
            
        
                
            
            gradient = gradientClass(learningRate= 0.001, gamma = 0.9, beta1=0.9, beta2=0.999)
            gradient.descent(x_0, function)
    
