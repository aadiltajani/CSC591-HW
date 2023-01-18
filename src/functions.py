import math

# Numerics
Seed = 937162211

def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo = 0, hi = 1):
    global Seed
    Seed = (16807 * (Seed)) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647

def rnd(n, places = 3):

    mult = 10 ** places
    return math.floor(n * mult + 0.5) / mult

# Lists
def map(t, fun):
    u = {}
    for k,v in t.items():
        v,k = fun(v)
        if k in u.keys():
            u[k] = v
        else:
            u[len(u) + 1] = v
    return u

def kap(t, fun):
    u = {}
    for k,v in t.items():
        v,k = fun(k,v)
        if k in u.keys():
            u[k] = v
        else:
            u[len(u) + 1] = v
    return u 

def sort(t):
    t = sorted(t)
    return t

def keys(t):
    return sorted(t.keys())