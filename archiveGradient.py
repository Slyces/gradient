#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:47:40 2018

@author: 3415104
"""


# Nesterov gradient descent
def nesterovGradientDescent(x_0, function, gamma=0.9, learningRate=1e-3, maxIter=10000):
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)

   utils.vprint("Starting position :", currentX)
   print("Nesterov")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX)]
   listeVariation = [np.array([1e-5 for i in range(dim)])]

   # @TODO : test de convergence ϵ
   for i in range(maxIter):
       variation = function.gradient(currentX-gamma*listeVariation[i], h) * learningRate + gamma*listeVariation[i]
       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
       listeVariation.append(np.copy(variation))

       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))
       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)

   return np.array(listeX)

# Momentum gradient descent
def momentumGradientDescent(x_0, function, gamma=0.9, learningRate=1e-3, maxIter=10000):
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)

   utils.vprint("Starting position :", currentX)
   print("momentum")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX)]
   listeVariation = [np.array([1e-5 for i in range(dim)])]

   # @TODO : test de convergence ϵ
   for i in range(maxIter):
       variation = function.gradient(currentX, h) * learningRate + gamma*listeVariation[i]
       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
       listeVariation.append(np.copy(variation))
       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))

       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)

   return np.array(listeX)





# Adam gradient descent
# @TODO Comprendre les beta exposant t
def adamGradientDescent(x_0, function, beta1=0.9, beta2=0.999, learningRate=1e-3, maxIter=10000):
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)
   utils.vprint("Starting position :", currentX)
   print("Adam")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX), np.copy(currentX)]

   squareVariation = np.array([0 for i in range(dim)])
   variations = np.array([0 for i in range(dim)])

   # @TODO : test de convergence ϵ
   for i in range(maxIter):

       gradient = function.gradient(currentX, h)
       squareVariation = beta1*squareVariation + (1-beta1)*gradient
       variations = beta2*variations + (1-beta2)*gradient**2

       variation = (squareVariation/ np.sqrt(variations)) * learningRate

       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))
       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)
   print(currentX)
   return np.array(listeX)
                           
# RMSprop gradient descent
def rmspropGradientDescent(x_0, function, gamma=0.9, learningRate=1e-3, maxIter=10000):
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)
   utils.vprint("Starting position :", currentX)
   print("RMSprop")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX), np.copy(currentX)]

   # Initialisation de E[g]
   squareGradient = np.array([1e-8 for i in range(dim)])

   # @TODO : test de convergence ϵ
   for i in range(maxIter):

       gradient = function.gradient(currentX, h)

       squareGradient = gamma*squareGradient +(1-gamma)* gradient**2

       variation = (gradient*learningRate)/np.sqrt(squareGradient)

       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))
           
       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)
   print(currentX)
   return np.array(listeX)


# Adadelta gradient descent
def adadeltaGradientDescent(x_0, function, gamma=0.9, maxIter=10000):
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)   
   utils.vprint("Starting position :", currentX)
   print("adadelta")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX), np.copy(currentX)]

   # Initialisation de E[g] et E[O]
   squareGradient = np.array([1e-8 for i in range(dim)])
   squareParameterVariation = np.array([1e-3 for i in range(dim)])

   # @TODO : test de convergence ϵ
   for i in range(maxIter):

       gradient = function.gradient(currentX, h)

       squareGradient = gamma*squareGradient +(1-gamma)* gradient**2
       squareParameterVariation = gamma*squareParameterVariation + (1-gamma)* (listeX[-1]-listeX[-2])**2

       variation = (np.sqrt(squareParameterVariation)/ np.sqrt(squareGradient))*gradient

       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))
       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)
   print(currentX)
   return np.array(listeX)
        

# Adagrad gradient descent
def adagradGradientDescent(x_0, function, learningRate=1e-3, maxIter=10000):
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)
   
   utils.vprint("Starting position :", currentX)
   print("dadagrad")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX)]

   # Initiliasation de Gt (somme des carrées des gradients trouvé jusqu'à lors pour chaque paramètre)
   squareGradient = np.array([1e-8 for i in range(dim)])

   # @TODO : test de convergence ϵ
   for i in range(maxIter):

       gradient = function.gradient(currentX, h)
       squareGradient += gradient ** 2
       variation = (gradient/ np.sqrt(squareGradient))*learningRate

       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire
       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))
       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)

   print(currentX)
   return np.array(listeX)


# Batch gradient descent
def batchGradientDescent(x_0, function, learningRate=1e-3, maxIter=10000):
   """ The gradient descent classic algorithm """
   # constantes
   h = 0.0001 # Variation nécéssaire au calcul du gradient
   dim = len(x_0)
   currentX = np.array(x_0, dtype=np.float64)

   utils.vprint("Starting position :", currentX)
   print("batch")
   # Initialisation de la liste des valeurs trouvées
   listeX = [np.copy(currentX)]

   # @TODO : test de convergence ϵ
   for i in range(maxIter):
       variation = function.gradient(currentX, h) * learningRate
       currentX -= variation # Modification de X
       listeX.append(np.copy(currentX)) # On garde la valeur de x en mémoire

       if i % 500 == 0:
           utils.vprint("Itération {} : {}".format(i, currentX ))
       if sum([0 if abs(k) < 0.0001 else 1 for k in variation]) == 0:
           print("fin", i, currentX)
           return np.array(listeX)
   print(currentX)
   return np.array(listeX)