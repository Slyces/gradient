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
            gradJ = (self.__call__(*(x + delta)) - self.__call__(*x)) / h
            gradient = np.append(gradient, [gradJ])
        return gradient

    # ---------------------------- implement this ---------------------------- #

    def_space = [] # definition space: [[x₁_min, x₁_max],
                                      # [x₂_min, x₂_max],
                                      # [     ...      ],
                                      # [x𝑛_min, x𝑛_max]] for an 𝑛 dimensional
                                      #                   function

    default_start = [] # default start  : np.array of size (dim)

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

    args = 'x'
    formula = '(x + 5)^2'

    def __call__(self, x):
        return (x + 5) * (x + 5)

square = square()

#                                                 _______
# ------------------ a sin in 2 dimensions : sin(√𝑥² + 𝑦²) ------------------- #
class sin2d(Function):
    def_space = [[-5, 5], [-5, 5]]
    default_start = [0.1, 1.5]

    args = 'x,y'
    formula = 'sin(\sqrt{x^2 + y^2})'

    def __call__(self, x, y):
        return np.sin(np.sqrt(x * x + y * y))

sin2d = sin2d()

# ---------------------------- Ackley's function ----------------------------- #
class ackley(Function):
    def_space = [[-5, 5], [-5, 5]]
    default_start = [4.5, 4.5]

    args = 'x,y'
    formula = '-20 exp[-0.2\sqrt{0.5 (x^2 + y^2)}]' \
            ' - exp[0.5 (cos2\pi x + cos2\pi y)] + e + 20'

    def __call__(self, x, y):
        return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x * x + y * y))) - np.exp(0.5 * (np.cos(2 * np.pi * x) \
                + np.cos(2 * np.pi * y))) + np.exp(1) + 20
ackley = ackley()
