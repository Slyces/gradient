# -------------------------------- utils file -------------------------------- #
verbose = 0

def vprint(*args, v=1):
    if verbose >= v:
        print(*args)

def isClose(a, b, rel_tol=1e-03, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def isFar(a, b, rel_tol=1e-03, abs_tol=0.0):
    return abs(a-b) >= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def isFarLower(a, b, rel_tol=1e-03, abs_tol=0.0):
    return b - a >= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def better_descent(v1, it1, v2, it2):
    return isFarLower(v1, v2) or (isClose(v1, v2) and it1 < it2)
