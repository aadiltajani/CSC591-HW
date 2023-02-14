import json
import math
import csv
import sys
from copy import deepcopy
import data
import NUM
import sym
import row
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
    if(type(t) == dict):
        for k,v in t.items():
            v = fun(v)
            if k is None:
                k = 1+len(u)
            u[k] = v 
        return u
    else:
        for k,v in enumerate(t):
            v = fun(v)
            if k is None:
                k = 1+len(u)
            u[k] = v 
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
    if(type(t) == NUM.NUM):
        return t.__dict__
    elif(type(t) == sym.sym):
        return t.__dict__
    elif(type(t) == row.Row):
        return t.__dict__
    
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

def last(t):
    if type(t) == dict:
        x = list(t.values())[-1]
    else:
        x = t[-1] 
    return x


def show(node, nPlaces, lvl = 0):

    if node:
        s = "|.." * lvl
        print(s, end="")
        if not node.get('left'):
            print(last(last(node["data"].rows).cells))
        else:
            print(str(int((100 * node["c"]))))
        show(node.get("left"), nPlaces, lvl + 1)
        show(node.get("right"), nPlaces, lvl + 1)

def copy(t):
    if isinstance(t, list) or isinstance(t, dict):
        return deepcopy(t)

def repRows(t, rows):
    rows = copy(rows)
    for j,s in enumerate(rows[len(rows)-1]):
        rows[0][j] = str(rows[0][j]) + ' : ' + str(s)
    rows.pop()
    for n,row in enumerate(rows):
        if n==0:
            row.append('thingX')
        else:
            u = t.get('rows')[len(t.get('rows')) -n]
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

def transpose(t):
    u = []
    for i in range(len(t[0])):
        row = []
        for j in t:
            row.append(j[i])
        u.append(row)
    return u

def dofile(fileName):
    with open(fileName) as f:
        return json.load(f)

def repCols(cols):
    cols = copy(cols)
    for i, col in enumerate(cols):
        col[-1] = str(col[0]) + ":" + str(col[-1])
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
    cols.insert(0, [f"Num{j}" for j in range(1, len(cols[0])+1)])    
    cols[0][-1] = "thingX"
    # cols = {k:{j:l for j,l in enumerate(v)} for k,v in enumerate(cols)}
    return data.DATA(cols)
