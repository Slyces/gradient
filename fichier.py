#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from algorithms import *
"""
Import des données
Retourne le gradient associé
"""
def importDonnees(nom):
    with open(nom, "r") as fichier:
        gradient = GradientDescent()
        entete = fichier.readline()
        
        ligne = fichier.readline()
        while ligne[0] != "P":
            pts, valeur = ligne.split(";")
            
            gradient.valeurs.append(float(valeur))
            point = pts.split(" ")
            gradient.points.append(float(point))
            
            ligne = fichier.readline()
        
        ligne = fichier.readline() # Points et valeurs optimals        
        
        ligne = fichier.readline()
        ligne = fichier.readline()
        temps, iter = ligne.split(";")
        gradient.tempsDescent = float(temps)
    
    return dic



"""
nom : nom du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
parameters1 : Les parametres du gradient
parameters2 : Les parametres de la descent
""" 
def creerDonnees(nom, gradient):
    with open(nom, "w") as fichier:
        # Ecriture dans le fichier
        

        s = "Point;Valeur\n"
        fichier.write(s)
       
        
        for i in range(len(gradient.points)):
            s=""
            pts = gradient.points[i]
            for v in pts:
                s+=str(v)+" "
            s = s[:-1]
            s+=";"
            s+= str(gradient.valeurs[i])
            s=s[:-3]+"\n"
            
            fichier.write(s)
        

        s = "PointOptimal;ValeurOptimale\n"

        fichier.write(s)
   
        s= str(gradient.points[-1])+";"+str(gradient.valeurs[-1])+"\n"
        fichier.write(s)

        s= "Temps;Nb iteration\n"
        fichier.write(s)
        
        s= str(gradient.tempsDescent)+";"+str(gradient.iteration)
        fichier.write(s)
        
"""
nom : nom du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
parameters1 : Les parametres du gradient
parameters2 : Les parametres de la descent
""" 
def creerParameters(nom, gradient, parameters1, parameters2):
    with open(nom, "w") as fichier:
        fichier.write(gradient.nom+"\n")
        fichier.write(str(parameters1)+"\n")
        fichier.write(str(parameters2)+"\n")

"""
nom : nom du fichier ou sauvegarder les données
gradient : L'algorithme de descente de gradient à utiliser
parameters1 : Les parametres du gradient
parameters2 : Les parametres de la descent
""" 
def creerDonneesLisible(nom, gradient):
    with open(nom, "w") as fichier:
        # Nom du gradient
        fichier.write(gradient.nom+"\n")
        # Point et valeur optimale
        fichier.write("La descente de gradient c'est arrêtée au point "+str(gradient.points[-1])+" de valeur "+str(gradient.valeurs[-1])+"\n")
        # Temps de calcul
        fichier.write("Le temps de calcul est "+str(gradient.tempsDescent)+"\n")
        # Nombre d'itération
        fichier.write("Il y a eu "+str(gradient.iteration)+" iterations\n")
        # Other useful data 
                
        