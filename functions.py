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

    # ---------------------------- implement this ---------------------------- #

    def_space = [] # definition space: [[x₁_min, x₁_max],
                                      # [x₂_min, x₂_max],
                                      # [     ...      ],
                                      # [x𝑛_min, x𝑛_max]] for an 𝑛 dimensional
                                      #                   function

    default_start = [] # default start  : np.array of size (dim)

    args = '𝑥'
    formula = '∅'

    def __call__(self, *args):
        pass

# /!\ for every function implementing this abstract class, add :
# /!\       MyFunc = MyFunc()
# /!\ to make it a Singleton

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
