import numpy as np
# ------------------- general model to declare a function -------------------- #
class Function(object):
    """Abstract class defining the structure of a function class"""
    # ------------------------ do not implement this ------------------------- #
    functions = {}
    def __init__(self): # init adds new functions to a list
        if type(self) != Function:
            Function.functions[type(self).__name__] = self

    @property
    def dim(self):
        return len(self.def_space)

    def __str__(self):
        return "{}\ ∶\ {} \longrightarrow {}".format(type(self).__name__, self.args,
                self.formula)

    def gradient(self, x, h=0.0001):
        gradient = np.array([])
        dim = len(x)
        # Computing the gradient for each dimension
        for j in range(dim):
            # @TODO: mieux commenter
            # Création de la variation : [0 .. h .. 0] (valeur h en position k)
            delta = np.array([0 if k != j else h for k in range(dim)])
            gradJ = (self(*(x + delta)) - self(*x)) / h
            gradient = np.append(gradient, [gradJ])
        return gradient

    # ---------------------------- implement this ---------------------------- #

    def_space = [] # definition space: [[x₁_min, x₁_max],
                                      # [x₂_min, x₂_max],
                                      # [     ...      ],
                                      # [x𝑛_min, x𝑛_max]] for an 𝑛 dimensional
                                      #                   function

    default_start = [] # default start  : np.array of size (dim)
    name = "" # name of the function
    args = '∅'
    formula = '∅'

    def __call__(self, *args):
        pass

# /!\ for every function implementing this abstract class, add :
# /!\       MyFunc = MyFunc()
# /!\ to make it a Singleton

# ----------------------------- custom functions ----------------------------- #

# -------------------- the 1D square function : (𝑥 + 5)² --------------------- #
class square(Function):
    def_space = [[-10, 0]]
    default_start = [-8]
    name = "square"
    args = 'x'
    formula = '(x + 5)^2'

    def __call__(self, x):
        return np.power(x+5,2)

square = square()

#                                                 _______
# ------------------ a sin in 2 dimensions : sin(√𝑥² + 𝑦²) ------------------- #
class sin2d(Function):
    def_space = [[-5, 5], [-5, 5]]
    default_start = [0.1, 1.5]
    name = "sin2d"
    args = 'x,y'
    formula = 'sin(\sqrt{x^2 + y^2})'

    def __call__(self, x, y):
        return np.sin(np.sqrt(np.power(x,2)+ np.power(y,2)))

sin2d = sin2d()

"""
Many Local Minima
"""
# ---------------------------- Ackley's function ----------------------------- #
class ackley(Function):
    def_space = [[-5, 5], [-5, 5]]
    default_start = [4.5, 4.5]
    name = "ackley"
    args = 'x,y'
    formula = '-20 exp[-0.2\sqrt{0.5 (x^2 + y^2)}]' \
            ' - exp[0.5 (cos2\pi x + cos2\pi y)] + e + 20'

    def __call__(self, x, y):
        return -20 * np.exp(-0.2 * np.sqrt(0.5 * (np.power(x,2) + np.power(y,2)))) - np.exp(0.5 * (np.cos(2 * np.pi * x) \
                + np.cos(2 * np.pi * y))) + np.exp(1) + 20

ackley = ackley()

# ---------------------------- bukin's function ----------------------------- #
class bukin(Function):
    def_space = [[-15, -5], [-3, 3]]
    default_start = [-7, 0]
    name = "bukin"
    args = 'x,y'
    formula = '100 * sqrt(abs(y - 0.01 * x)) + 0.01 * abs(x + 10)'

    def __call__(self, x, y):
        return 100 * np.sqrt(abs(y - 0.01 * np.power(x,2))) + 0.01 * abs(x + 10)

bukin = bukin()


# ---------------------------- crossintray's function----------------------------- 
class crossintray(Function):
    def_space = [[-10, 10], [-10, 10]]
    default_start = [-0, 0]
    name = "crossintray"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return -0.0001 * np.power(abs(np.sin(x) * np.sin(y) * np.exp(abs(100 - np.sqrt(np.power(x,2)+np.power(y,2)) / np.pi)) + 1), 0.1)

crossintray = crossintray()



# ---------------------------- dropwave's function----------------------------- 
class dropwave(Function):
    def_space = [[-5.12, 5.12], [-5.12, 5.12]]
    default_start = [-2, 3]
    name = "dropwave"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return - (1 + np.cos(12 * np.sqrt(np.power(x,2) + np.power(y,2)))) / (0.5 * (np.power(x,2) + np.power(y,2)) + 2)

dropwave = dropwave()

# ---------------------------- holdertable's function----------------------------- 
class holdertable(Function):
    def_space = [[-10, 10], [-10, 10]]
    default_start = [-4, 3]
    name = "holdertable"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return - abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - np.sqrt(np.power(x,2) + np.power(y,2)) / np.pi)))

holdertable = holdertable()

"""
Bowl-Shaped
"""

# ---------------------------- bohachevsky's function----------------------------- 
class bohachevsky(Function):
    def_space = [[-100, 100], [-100, 100]]
    default_start = [-75, 26]
    name = "bohachevsky"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return np.power(x, 2) + 2*np.power(y, 2) - 0.3 * np.cos(3*np.pi*x)-0.4*np.cos(4*np.pi*y) * 0.7
        
bohachevsky = bohachevsky()



"""
Plate-Shaped
"""

# ---------------------------- booth's function----------------------------- 
class booth(Function):
    def_space = [[-10, 10], [-10, 10]]
    default_start = [-7, 6]
    name = "booth"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return np.power((x + 2 * y - 7), 2) + np.power(2 * x + y - 5, 2)

booth = booth()


# ---------------------------- matyas's function----------------------------- 
class matyas(Function):
    def_space = [[-10, 10], [-10, 10]]
    default_start = [-7, 6]
    name = "matyas"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return 0.26 * (np.power(x, 2) + np.power(y, 2)) - 0.48 * x * y

matyas = matyas()


# ---------------------------- threehumpcamel's function----------------------------- 
class threehumpcamel(Function):
    def_space = [[-5, 5], [-5, 5]]
    default_start = [2, -2.5]
    name = "threehumpcamel"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return 2 * np.power(x, 2) - 1.05 * np.power(x, 4) + (1/6) * np.power(x, 6) + x * y + np.power(y, 2)

threehumpcamel = threehumpcamel()

"""
Saddle point
"""
# ---------------------------- hessian's function----------------------------- 
class hessian(Function):
    def_space = [[-5, 5], [-5, 5]]
    default_start = [0,0]
    name = "hessian"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        f = np.power(x, 2) - np.power(y, 2)
        if f > -10.0:
            return f
        else:
            return -10.0
hessian = hessian()

# ---------------------------- beale's function----------------------------- 
class beale(Function):
    def_space = [[-4, 5], [-4, 5]]
    default_start = [0.01, -0.5]
    name = "beale"
    args = 'x,y'
    formula = ''

    def __call__(self, x, y):
        return np.power(1.5 - x + x * y, 2) + np.power(2.25 - x + x * np.power(y, 2), 2) + np.power(2.625 - x + x * np.power(y, 3), 2)

beale = beale()


# -------------------- the 1D cube function : 𝑥^3 --------------------- #
class cube(Function):
    def_space = [[-5, 5]]
    default_start = [1]
    name = "cube"
    args = 'x'
    formula = 'x^3'

    def __call__(self, x):
        min_threshold = -30.0
        x3 = np.power(x,3)
        if x3 > min_threshold:
            return x3
        else:
            return min_threshold
cube = cube()


# -------------------- momentum --------------------- #
class p42m(Function):
    def_space = [[-3, 3]]
    default_start = [-3]
    name = "p42m"
    args = 'x'
    formula = 'x^4 - 3 * x^2 + x'

    def __call__(self, x):
        return  np.power(x, 4) - 4*np.power(x, 2) + x
p42m = p42m()





