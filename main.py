import numpy as np
import matplotlib.pyplot as plt
from functions import *
import utils
from time import time
from algorithms import *
import os
from fichier import *

from random import uniform

def generationDeDonnees():
   
   dossier = "Donnees"
   epislon = 0.001 # la marge d'erreur
   nbPoints = 10
   
   
   # Pour chaque fonction
   # Pour différent point
   # Pour différent algorithm
   # Pour différent paramètre
   
   functions = [sin2d, square, ackley]
   algorithms = [BatchGradientDescent, MomentumGradientDescent, NesterovGradientDescent, AdagradGradientDescent, AdadeltaGradientDescent, RmspropGradientDescent, AdamGradientDescent]
   
   # Les valeurs des différents paramètre à étudier
   learningRates = [0.0001+0.0001*i**2 for i in range(50)]
   gammas =  [0.99-0.001*i**2 for i in range(20)]
   beta1s = [0.80, 0.85, 0.9, 0.95, 0.99]
   beta2s = [0.9, 0.95,0.999, 0.9999]

   
   for function in functions:
      print("Generation de la fonction "+function.name)
      if not os.path.exists(dossier+"/"+function.name):
         os.makedirs(dossier+"/"+function.name)
         
      points = [[uniform(v[0],v[1]) for v in function.def_space] for i in range(nbPoints)]
      
      for point in points:
         print("Generation du point"+str(point))
         if not os.path.exists(dossier+"/"+function.name+"/"+str(point)):
            os.makedirs(dossier+"/"+function.name+"/"+str(point))
            
         for algorithm in algorithms:
            print("Generation de l'algorithme"+algorithm.nom)
            if not os.path.exists(dossier+"/"+function.name+"/"+str(point)+"/"+algorithm.nom):
               os.makedirs(dossier+"/"+function.name+"/"+str(point)+"/"+algorithm.nom)
            
            
            # On regarde si ça vaut la peine d'étudier tout les parametres
            params = []
            if "learningRate"in algorithm.param:
               params.append(learningRates)
            else:
               params.append([0])
            if "gamma"in algorithm.param:
               params.append(gammas)
            else:
               params.append([0])
            if "beta1"in algorithm.param:
               params.append(beta1s)
            else:
               params.append([0])
            if "beta2"in algorithm.param:
               params.append(beta2s)
            else:
               params.append([0])
            
            param1 = {}
            param2 = {}
            bestGradient = 0
            # Pour toute les possibilités de paramêtre
            for learningRate in params[0]:
               for gamma in params[1]:
                  for beta1 in params[2]:
                     for beta2 in params[3]:
                        
                        # Calcul du gradient
                        gradient = algorithm(learningRate=learningRate, gamma=gamma, beta1=beta1, beta2=beta2)
                        gradient.descent(point, function)
                        
                        # On garde seulement si c'est meilleur
                        # Si il n'y a pas de gradient
                        # Si il converge vers un bien meilleur valeur
                        # Si il converge au même endroit mais qu'il le fait plus vite
                        
                        if bestGradient ==0 or bestGradient.valeurs[-1] - gradient.valeurs[-1] > epsilon or (abs(gradient.valeurs[-1] - bestGradient.valeurs[-1]) < epsilon*0.1 and gradient.iteration < bestGradient.iteration):
 
                           # Préparer les paramêtres pour les conserver
                           param1 = {"learningRate":learningRate, "gamma":gamma, "beta1":beta1, "beta2":beta2}
                           param2 = {"x_0":point, "function":function}
                           bestGradient = gradient

            dos = dossier+"/"+function.name+"/"+str(point)+"/"+algorithm.nom+"/"
   
            # Génération des données
            creerDonnees(dos+"/Donnees.txt", bestGradient)
            creerParameters(dos+"/Parametres.txt", bestGradient, param1, param2)
            creerDonneesLisible(dos+"/DonneesLisible.txt", bestGradient)
            
"""
Lancement du programme
"""
if __name__ == '__main__':
   generationDeDonnees()
   
   

   
