import numpy as np
import matplotlib.pyplot as plt
from functions import *
import utils
from time import time
from algorithms import *


        

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
   
   creerDonnees(dos+"Data", batch, parameters1, parameters2)
   creerParameters(dos+"Param", batch, parameters1, parameters2)
   creerDonneesLisible(dos+"Lisible", batch, parameters1, parameters2)
   
