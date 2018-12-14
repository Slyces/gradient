import numpy as np
import utils
from time import time

# --------------- descent object wrapping stats of the descent --------------- #
class GradientDescent(object):
    
   nom = ""
    
   """Wrapper class containing statistics about the descent"""
   def __init__(self, **kwargs):
       """Void init, the descent must be completed sequentially"""
       self.points = [] # record every points of the descent
       self.variations = [] # record every variations of the point
       self.valeurs = [] # record every value of the fonction
       
       learningRate = kwargs.get("learningRate", None)
       if learningRate:
           self.learningRate = learningRate
           
       gamma = kwargs.get("gamma", None)
       if gamma:
           self.gamma = gamma

       beta1 = kwargs.get("beta1", None)
       if beta1:
           self.beta1 = beta1

       beta2 = kwargs.get("beta2", None)
       if beta2:
           self.beta2 = beta2

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

   def descent(self, x_0, function, maxIter=1000, maxTime=1e10, epsilon=1e-5):
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

       self.add_point(np.copy(currentX)) # On garde la valeur de x en mémoire
       self.variations.append(np.copy(variation))
       self.valeurs.append(self.function(*self.points[-1]))
       # --------------------- LANCEMENT DE LA DESCENTE --------------------- #
       t = 0
       while t < self.maxIter and (time() - self.tempsStart) < self.maxTime and \
               np.linalg.norm(variation) >= epsilon:
           variation = self.getVariation(currentX)
           currentX -= variation
           
           self.add_point(np.copy(currentX))# On garde la valeur de x en mémoire
           self.variations.append(np.copy(variation))
           self.valeurs.append(self.function(*self.points[-1]))
           t += 1

           if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
               self.iteration = t
               self.tempsDescent = time() - self.tempsStart     
               return self.points
                
       self.iteration = t
       self.tempsDescent = time() - self.tempsStart     
       return self.points

   def getVariation(self, x):
       return self.function.gradient(x, self.h)

# --------------- Batch Descent --------------- #  
class BatchGradientDescent(GradientDescent):
    
    
   nom = "batch"
   param = ["learningRate"]
   
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)

       
   def getVariation(self, x):
       return self.function.gradient(x, self.h)*self.learningRate

# --------------- Momentum Descent --------------- #  
class MomentumGradientDescent(GradientDescent):
    
   nom = "momentum"
   param = ["learningRate", "gamma"]
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)

   def getVariation(self, x):
       return self.function.gradient(x, self.h) * self.learningRate \
               + self.gamma * self.variations[-1]

# --------------- Nesterov Descent --------------- #  
class NesterovGradientDescent(GradientDescent):
    
   nom = "nesterov"
   param = ["learningRate", "gamma"]    
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)

    
   def getVariation(self, x):
       return self.function.gradient(x - self.gamma * self.variations[-1],  self.h) * self.learningRate \
               + self.gamma * self.variations[-1]


# --------------- Adagrad Descent --------------- #  
class AdagradGradientDescent(GradientDescent):

   nom = "adagrad"
   param = ["learningRate"]
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)



       self.squareGradient = 0.1

   def getVariation(self, x):
       if type(self.squareGradient) == float:
           self.squareGradient = np.array([1e-8 for i in range(self.dim)])       
       
       gradient = self.function.gradient(x,  self.h)
       self.squareGradient += gradient ** 2
       return (gradient / np.sqrt(self.squareGradient))* self.learningRate
   

# --------------- Adadelta Descent --------------- #  
class AdadeltaGradientDescent(GradientDescent):

   nom = "adadelta"
   param = ["learningRate", "gamma"]
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)


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
class RmspropGradientDescent(GradientDescent):
   
   nom = "rmsprop"
   param = ["learningRate", "gamma"]   
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)


       self.squareGradient = 0.1
       
   def getVariation(self, x):
       if type(self.squareGradient) == float:
           self.squareGradient = np.array([1e-8 for i in range(self.dim)])

       gradient = self.function.gradient(x,  self.h)
       self.squareGradient = self.gamma * self.squareGradient + (1-self.gamma) * gradient **2

       return gradient * self.learningRate / np.sqrt(self.squareGradient)

# --------------- Adam Descent --------------- #  
class AdamGradientDescent(GradientDescent):

   nom = "adam"
   param = ["learningRate", "beta1", "beta2"]
   def __init__(self, **kwargs):
       GradientDescent.__init__(self, **kwargs)

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
   

# ----------------------- gradient descent algorithms ------------------------ #
implemented = ['batch', 'momentum', 'nesterov', 'adagrad', 'adadelta', 'rmsprop', 'adam']
h = 10e-4 # Variation nécéssaire au calcul du gradient
epsilon = 5 * 10e-5
