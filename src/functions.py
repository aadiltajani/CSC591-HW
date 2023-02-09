import math
import csv
import sys
from copy import deepcopy
import data
sys.path.append("./src")


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
    for v in t:
        v, k = fun(t.index(v), v)
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
    if (not isinstance(t, dict)) and (not isinstance(t, list)):
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


def typecheck(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        pass
    else:
        return b
    try:
        a = float(x)
    except (TypeError, ValueError):
        return x
    else:
        return float(x)


def csv_read(filename):
    f = open(filename, 'r')
    # f = open(r'./etc/data/auto93.csv', 'r')

    reader = csv.reader(f)
    t = []
    for row in reader:
        t.append([typecheck(ele) for ele in row])
    # if fun is not None:
    #     fun(t)
    return t

def cosine(a,b,c):
    den = 1 if c == 0 else 2 * c
    x1 = (a**2 + c**2 - b**2) / den
    x2 = max(0, min(1, x1))
    y = abs((a**2 - x2**2)) ** 0.5
    return x2, y

def show(node, what, cols, nPlaces, lvl = 0):

    if node:
        s = "| " * lvl
        print(s+ str(len(node.rows)) + " ")
        if not hasattr(node, 'left'):
            print(o(node.stats("mid",node.cols.y,nPlaces)))
        elif lvl == 0 :
            print(o(node.stats("mid",node.cols.y,nPlaces)))
        if hasattr(node, 'left'):
            show(node.left, what,cols, nPlaces, lvl+1)
        else:
            show(None, what,cols, nPlaces, lvl+1)
        if hasattr(node, 'right'):
            show(node.right, what,cols,nPlaces, lvl+1)
        else:
            show(None, what,cols,nPlaces, lvl+1)
    else:
        pass

def copy(t):
    if isinstance(t, list) or isinstance(t, dict):
        return deepcopy(t)

def repRows(t, rows, u):
    rows = copy(rows)
    for j,s in enumerate(rows[len(rows)-1]):
        rows[1][j] = rows[1][j] + ' : ' + s
    rows[len(rows)-1] = None
    for n,row in enumerate(rows):
        if n==1:
            row.append('thingX')
        else:
            u = t.rows[len(t.rows) - 1 - n + 2]
            row.append(u[len(u)-1])
    return data.DATA(rows)

def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i] = {}
        for j in range(1, n+1):
            g[i][j] = " "
    maxy = 0
    print("")
    for r,row in enumerate(data.rows):
        c = chr(64+r)
        print(c, row.cells[-1])
        x,y = ((row.x)*n)//1, ((row.y)*n)//1
        maxy = max(maxy, y+1)
        g[y+1][x+1] = c
    print("")
    for y in range(1, maxy):
        oo(g[y])
 
def repgrid(sFile):
    t = dofile(sFile)
    rows = repRows(t, transpose(t.cols))
    cols = repCols(t.cols)
    print(rows.cluster())
    print(cols.cluster())
    repPlace(rows)

def repCols(cols):
    cols = copy(cols)
    for col in cols:
        col[-1] = f"{col[0]}:{col[-1]}"
        col[:-1] = col[1:]
        col.pop()
    cols.insert(0, ["Num" + str(i) for i in range(len(cols[0]))])
    cols[0][-1] = "thingX"
    return data.DATA(cols)
