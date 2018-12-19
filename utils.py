# -------------------------------- utils file -------------------------------- #
verbose = 0

def vprint(*args, v=1):
    if verbose >= v:
        print(*args)

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
 

def isClose(a, b, rel_tol=1e-02, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def isFar(a, b, rel_tol=1e-02, abs_tol=0.0):
    return abs(a-b) >= max(rel_tol * max(abs(a), abs(b)), abs_tol)