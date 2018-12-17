#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:05:54 2018

@author: 3415104
"""

import numpy as np, utils, os


def getData(directory):
    
    if not os.path.exists(directory):
        print("Directory doesn't exist")
        return
    
    else:
        points = []
        descents = []
        
        for point in os.listdir(directory):
            # Si il s'agit bien d'un dossier
            point_directory = os.path.join(directory,point)
            
            if os.path.isdir(point_directory):
                # We try if the point is completely calculated
                
                if pointIsComplete(point_directory):

                    points.append(point[1:-1].split(","))
                    
                    gradient_dictionnary = {}
                    for algorithm in os.listdir(point_directory):
                        algorithm_directory = os.path.join(point_directory, algorithm)
                        
                        gradient_dictionnary[algorithm] = {}
                        
                        with open(os.path.join(algorithm_directory, "raw_data.txt"), "r") as fichier:
                            data = fichier.readlines()[-4:]
                            
                            gradient_dictionnary[algorithm]["temps"] = data[-1].split(";")[0]
                            gradient_dictionnary[algorithm]["nb_iteration"] = data[-1].split(";")[1]
                            gradient_dictionnary[algorithm]["point_optimal"] = data[1].split(";")[0]
                            gradient_dictionnary[algorithm]["valeur_optimale"] = data[1].split(";")[1]
            
                    descents.append(gradient_dictionnary)
            
        return points, descents

def pointIsComplete(directory):
    
    if "adam" not in os.listdir(directory):
        print("L'algorithme adam n'a pas été lancé")
        return False
        
    elif "summary.txt" not in os.listdir(os.path.join(directory, 'adam')):
        print("L'algorithme adam n'est pas arrivé au bout")
        return False
        
    else:
        print("Point completely calculated")
        return True
