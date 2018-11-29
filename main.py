import numpy as np
import matplotlib.pyplot as plt
from functions import *
import utils
from time import time
from algorithms import *

"""
Import des données
Retourne un dictionnaire
"""
def importDonnees(nom):
    with open(nom, "r") as fichier:
        dic = {}
        entete = fichier.readline().split(" ; ")
        dicNom = {}
        for i in range(len(entete)):
            valeur = entete[i]
            val = valeur.split("_")
            dic[val[1]] = {}
            dic[val[1]]["Valeurs"] = []
            dic[val[1]]["Points"] = []
            
            dicNom[i//2] = val[1]
        
        ligne = fichier.readline()
        while ligne[0] != "P":
            valeur = ligne.split(" ; ")
            for i in range(len(valeur)//2):
                dic[dicNom[i]]["Valeurs"].append(float(valeur[i*2+1]))
                point = valeur[i*2].split(" ")
                dic[dicNom[i]]["Points"].append(point)
            
            ligne = fichier.readline()
        
        ligne = fichier.readline()
        valeur = ligne.split(" ; ")
        for i in range(len(valeur)//2):
            dic[dicNom[i]]["PointOptimal"] = valeur[i*2]
            dic[dicNom[i]]["ValeurOptimale"] = valeur[i*2+1]
        
        ligne = fichier.readline()
        ligne = fichier.readline()
        valeur = ligne.split(" ; ")
        for i in range(len(valeur)//2):
            dic[dicNom[i]]["Temps"] = valeur[i*2]
            dic[dicNom[i]]["Iteration"] = valeur[i*2+1]
    
    return dic



"""
nom : nom du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
parameters1 : Les parametres du gradient
parameters2 : Les parametres de la descent
""" 
def creerDonnees(nom, gradients, parameters1, parameters2):
    with open(nom, "w") as fichier:
        # Ecriture dans le fichier
        
        m = max([len(gradient.points) for gradient in gradients]) # Nombre maximum d'itération
        s=""
        for gradient in gradients:
            s += "Point_"+str(gradient)+" ; Valeur_"+str(gradient) + " ; "
        s = s[:-3]+"\n"
        fichier.write(s)
       
        
        for i in range(m):
            s=""
            for gradient in gradients:
                if i < len(gradient.points):
                    pts = gradient.points[i]
                    for v in pts:
                        s+=str(v)+" "
                    s+="; "
                    s+= str(gradient.valeurs[i])
                    s+=" ; "
            s=s[:-3]+"\n"
            
            fichier.write(s)
        
        s=""
        for gradient in gradients:
            s += "PointOptimal_"+str(gradient)+" ; ValeurOptimale_"+str(gradient) + " ; "
        s = s[:-3]+"\n"
        print(s)
        fichier.write(s)
   
        s=""
        for gradient in gradients:
            s += str(gradient.points[-1])+" ; "+str(gradient.valeurs[-1])+" ; "
        s = s[:-3]+"\n"
        fichier.write(s)

        s=""
        for gradient in gradients:
            s += "Temps_"+str(gradient)+" ; Nb iteration_"+str(gradient) + " ; "
        s = s[:-3]+"\n"
        fichier.write(s)
        
        s=""
        for gradient in gradients:
            s += str(gradient.tempsDescent)+" ; "+str(gradient.iteration)+" ; "
        s = s[:-3]+"\n"
        fichier.write(s)
        
"""
nom : nom du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
parameters1 : Les parametres du gradient
parameters2 : Les parametres de la descent
""" 
def creerParameters(nom, gradients, parameters1, parameters2):
    with open(nom, "w") as fichier:
        for gradient in gradients:
            fichier.write(str(gradient)+"\n")
            fichier.write(str(parameters1)+"\n")
            fichier.write(str(parameters2)+"\n\n")

"""
nom : nom du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
parameters1 : Les parametres du gradient
parameters2 : Les parametres de la descent
""" 
def creerDonneesLisible(nom, gradients,parameters1, parameters2):
    with open(nom, "w") as fichier:
        for gradient in gradients:
            # Nom du gradient
            fichier.write(str(gradient)+"\n")
            # Point et valeur optimale
            fichier.write("La descente de gradient c'est arrêtée au point "+str(gradient.points[-1])+" de valeur "+str(gradient.valeurs[-1])+"\n")
            # Temps de calcul
            fichier.write("Le temps de calcul est "+str(gradient.tempsDescent)+"\n")
            # Nombre d'itération
            fichier.write("Il y a eu "+str(gradient.iteration)+" iterations\n")
            # Other useful data 
            
            fichier.write("\n")
        
        
        

"""
Lancement du programme
"""
if __name__ == '__main__':
   x = [0.5, 0.5]
   f = sin2d


   batch = BatchGradientDescent()
   batch.descent(x, f)
   momentum = MomentumGradientDescent()
   momentum.descent(x, f)
   nesterov = NesterovGradientDescent()
   nesterov.descent(x, f)
   adagrad = AdagradGradientDescent()
   adagrad.descent(x, f)
   adadelta = AdadeltaGradientDescent()
   adadelta.descent(x, f)
   RMSprop = RMSpropGradientDescent()
   RMSprop.descent(x, f)
   adam = AdamGradientDescent()
   adam.descent(x, f)
   
   parameters1 = []
   parameters2 = [x, f]
   
   dos = "Donnees/"
   
   creerDonnees(dos+"Data", [batch, momentum, nesterov, adagrad, adadelta, RMSprop, adam], parameters1, parameters2)
   creerParameters(dos+"Param", [batch, momentum, nesterov, adagrad, adadelta, RMSprop, adam], parameters1, parameters2)
   creerDonneesLisible(dos+"Lisible", [batch, momentum, nesterov, adagrad, adadelta, RMSprop, adam], parameters1, parameters2)
   
   d = importDonnees(dos+"Data")
