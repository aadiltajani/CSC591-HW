import math

# Numerics
# Seed = 937162211


def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))


def rand(seed, lo=0, hi=1):
    
    seed = (16807 * (seed)) % 2147483647
    return lo + (hi - lo) * seed / 2147483647, seed 


def rnd(n, places=3):
    mult = 10 ** places
    return math.floor(n * mult + 0.5) / mult


# Lists
def map(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(v)
        if k in u.keys():
            u[k] = v
        else:
            u[len(u) + 1] = v
    return u


def kap(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(k, v)
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


# Strings
def oo(t):
    print(o(t))
    return True


def fmt(s, *a):
    return str.format(s, a)


def o(t):
    if ((not isinstance(t, dict)) and (not isinstance(t, list))):
        return str(t)

    def show(k, v):
        if str(k).find('_') != 0:
            v = o(v)
            return isinstance(t, dict) and (":" + str(k) + " " + str(v)) or str(v)

    u = []
    if isinstance(t, dict):
        for k, v in t.items():
            showop = show(k, v)
            if showop:
                u.append(showop)
            u.sort()

    elif isinstance(t, list):
        u = t
    return "{" + " ".join(str(val) for val in u) + "}"


def the(t):
    oo(t)
