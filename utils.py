# -------------------------------- utils file -------------------------------- #
verbose = 0

def vprint(*args, v=1):
    if verbose >= v:
        print(*args)
