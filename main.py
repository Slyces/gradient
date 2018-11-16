import numpy as np
import matplotlib.pyplot as plt
from functions import *
import utils
from time import time


# --------------- descent object wrapping stats of the descent --------------- #
class GradientDescent(object):

   """Wrapper class containing statistics about the descent"""
   def __init__(self):
       """Void init, the descent must be completed sequentially"""
       self.points = [] # record every points of the descent
       self.variations = [] # record every variations of the point

   # ----------- getters for first and last point of the descent ------------ #
   @property
   def start(self):
       return self.points[0]

   @property
   def stop(self):
       return self.points[-1]

   # --------------------- gradually adding statistics ---------------------- #
   def add_point(self, p):
       self.points.append(p)

   def descent(self, x_0, function, maxIter=10000, maxTime=1e10, epsilon=1e-8):
       # Initialisation des variables communes à toutes les descentes de gradient
       self.h = 0.0001 # Variation nécéssaire au calcul du gradient

       self.x_0 = np.array(x_0, dtype=np.float64) # Starting position
       self.dim = len(self.x_0) # Dimension of x_0
       self.function = function # function to minimize
       self.maxIter = maxIter # Maximum number of iteration
       self.tempsStart = time()
       self.maxTime = maxTime # Maximum time of iteration
       variation = np.array([epsilon * 1e3 for i in range(self.dim)])# Initialisation de la variation à v > ϵ
       currentX = np.array(self.x_0, dtype=np.float64)
       utils.vprint("Starting position :", currentX)

       self.add_point(np.copy(currentX))# On garde la valeur de x en mémoire
       self.variations.append(np.copy(variation))
       # --------------------- LANCEMENT DE LA DESCENTE --------------------- #
       t = 0
       while t < self.maxIter and (time() - self.tempsStart) < self.maxTime and \
               np.linalg.norm(variation) >= epsilon:
           variation = self.getVariation(currentX)
           currentX -= variation
           self.add_point(np.copy(currentX))# On garde la valeur de x en mémoire
           self.variations.append(np.copy(variation))
           t += 1

           if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
                return self.points

       return self.points

   def getVariation(self, x):
       return self.function.gradient(x, self.h)

# --------------- Batch Descent --------------- #  
class BatchGradientDescent(GradientDescent):
   def __init__(self, learningRate=1e-3):
       GradientDescent.__init__(self)

       self.learningRate = learningRate

   def getVariation(self, x):
       return self.function.gradient(x, self.h)*self.learningRate

# --------------- Momentum Descent --------------- #  
class MomentumGradientDescent(GradientDescent):
   def __init__(self, learningRate=1e-3, gamma=0.9):
       GradientDescent.__init__(self)

       self.learningRate = learningRate
       self.gamma = gamma

   def getVariation(self, x):
       return self.function.gradient(x, self.h) * self.learningRate \
               + self.gamma * self.variations[-1]

# --------------- Nesterov Descent --------------- #  
class NesterovGradientDescent(GradientDescent):
   def __init__(self, learningRate=1e-3, gamma=0.9):
       GradientDescent.__init__(self)

       self.learningRate = learningRate
       self.gamma = gamma

   def getVariation(self, x):
       return self.function.gradient(x - self.gamma * self.variations[-1],  self.h) * self.learningRate \
               + self.gamma * self.variations[-1]


# --------------- Adagrad Descent --------------- #  
class AdagradGradientDescent(GradientDescent):
   def __init__(self, learningRate=1e-3):
       GradientDescent.__init__(self)

       self.learningRate = learningRate
       self.squareGradient = 0.1

   def getVariation(self, x):
       if type(self.squareGradient) == float:
           self.squareGradient = np.array([1e-8 for i in range(self.dim)])       
       
       gradient = self.function.gradient(x,  self.h)
       self.squareGradient += gradient ** 2
       return (gradient / np.sqrt(self.squareGradient))* self.learningRate
   

# --------------- Adadelta Descent --------------- #  
class AdadeltaGradientDescent(GradientDescent):
   def __init__(self, gamma=0.9):
       GradientDescent.__init__(self)

       self.gamma = gamma
       self.squareGradient = 0.1
       self.squareParameterVariation = 0.1
       
   def getVariation(self, x):
       if type(self.squareGradient) == float:
           self.squareGradient = np.array([1e-8 for i in range(self.dim)])
           self.squareParameterVariation = np.array([1e-3 for i in range(self.dim)])
           
           
       gradient = self.function.gradient(x,  self.h)
       self.squareGradient = self.gamma * self.squareGradient + (1-self.gamma) * gradient **2
       self.squareParameterVariation = self.gamma * self.squareParameterVariation + (1-self.gamma)* self.variations[-1]**2
       return (np.sqrt(self.squareParameterVariation) / np.sqrt(self.squareGradient)) * gradient

# --------------- RMSprop Descent --------------- #  
class RMSpropGradientDescent(GradientDescent):
   def __init__(self, learningRate=1e-3, gamma=0.9):
       GradientDescent.__init__(self)

       self.gamma = gamma
       self.learningRate = learningRate
       self.squareGradient = 0.1
       
   def getVariation(self, x):
       if type(self.squareGradient) == float:
           self.squareGradient = np.array([1e-8 for i in range(self.dim)])

       gradient = self.function.gradient(x,  self.h)
       self.squareGradient = self.gamma * self.squareGradient + (1-self.gamma) * gradient **2

       return gradient * self.learningRate / np.sqrt(self.squareGradient)

# --------------- Adam Descent --------------- #  
class AdamGradientDescent(GradientDescent):
   def __init__(self, learningRate=1e-3, beta1=0.9, beta2=0.999):
       GradientDescent.__init__(self)

       self.learningRate = learningRate
       self.beta1 = beta1
       self.beta2 = beta2
       self.squareVariation = 0.1
       self.simpleVariation = 0.1
       
   def getVariation(self, x):
       if type(self.squareVariation) == float:
           self.squareVariation = np.array([0 for i in range(self.dim)])
           self.simpleVariation = np.array([0 for i in range(self.dim)])
           
       gradient = self.function.gradient(x,  self.h)
       self.squareVariation = self.beta2*self.squareVariation + (1-self.beta2)*gradient**2
       self.simpleVariation = self.beta1*self.simpleVariation + (1-self.beta1)*gradient

       return self.simpleVariation * self.learningRate / np.sqrt(self.squareVariation)

"""
Lancement du programme
"""
if __name__ == '__main__':
   x = [1, 0.5]
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
