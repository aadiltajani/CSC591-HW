import json
import math
import csv
import sys
from copy import deepcopy
import data
import NUM
import SYM
import sym
import row
import col
sys.path.append("./HW-5/src")

def range(at, txt, lo, hi):
    d = {
        'at' : at,
        'txt' : txt,
        'lo' : lo,
        'hi' : lo or hi or lo,
        'y' : SYM.SYM()
    }

def add(col,x):
    if x != "?":
        n=1
        col['n'] = col['n'] + n
        if col['isSym']:
            col['has']['x'] = n + (col['has']['x'] or 0)
            if col['has']['x'] > col['most']:
                col['most'], col['mode'] = col['has']['x'],x
            else:
                col['lo'], col['hi'] = math.min(x,col['lo']), math.max(x,col['hi'])
                all = len(col['has'])
                pos = (all < 512 and all+1) or (function.rand() < 512/col['n'] and function.rint(1,all))
                if pos:
                    col['has'][pos] = x
                    col['ok'] = False


def adds(col, t):
    for _,x in enumerate(t):
        add(col, x)
    return col

def extend(range, n, s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])

    add(range['y'], s)
    

def has(col):
    if not col['isSym'] and not col['ok']:
        col['has'] = dict(sorted(col['has']))
    col['ok'] = True
    return col['has']
    

def per(t, p=0.5):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(0, min(len(t), p - 1))] 

# Numerics
# Seed = 937162211


# def rint(lo, hi):
#   return math.floor(0.5 + rand(lo, hi))

# global Seed


# def rand(lo, hi):
#   Seed =  93716211
#   lo = lo or 0
#   hi = hi or 1
#   Seed = (16807 * Seed) % 2147483647
#   return lo + (hi - lo) * Seed / 2147483647

# def rnd(n, places=3):
#     mult = 10 ** places
#     return math.floor(n * mult + 0.5) / mult


# # Lists
# def map(t, fun):
#     u = {}
#     if(type(t) == dict):
#         for k,v in t.items():
#             v = fun(v)
#             if k is None:
#                 k = 1+len(u)
#             u[k] = v 
#         return u
#     else:
#         for k,v in enumerate(t):
#             v = fun(v)
#             if k is None:
#                 k = 1+len(u)
#             u[k] = v 
#         return u


# def many(t, n):
#     u = []
#     for i in range(n):
#         u.append(any(t))

# def kap(t, fun):
#     u = {}
#     for v in t:
#         v, k = fun(t.index(v), v)
#         if k in u.keys():
#             u[k] = v
#         else:
#             u[len(u) + 1] = v
#     return u


# def sort(t):
#     t = sorted(t)
#     return t


# def keys(t):
#     return sorted(t.keys())


# # Strings
# def oo(t):
#     print(o(t))
#     return True


# def fmt(s, *a):
#     return str.format(s, a)


# def o(t):
#     if(type(t) == NUM.NUM):
#         return t.__dict__
#     elif(type(t) == sym.sym):
#         return t.__dict__
#     elif(type(t) == row.Row):
#         return t.__dict__
    
#     if (not isinstance(t, dict)) and (not isinstance(t, list)):
#         return str(t)


#     def show(k, v):
#         if str(k).find('_') != 0:
#             v = o(v)
#             return isinstance(t, dict) and (":" + str(k) + " " + str(v)) or str(v)

#     u = []
#     if isinstance(t, dict):
#         for k, v in t.items():
#             showop = show(k, v)
#             if showop:
#                 u.append(showop)
#             u.sort()

#     elif isinstance(t, list):
#         u = t
#     return "{" + " ".join(str(val) for val in u) + "}"


# def the(t):
#     oo(t)


# def typecheck(x):
#     try:
#         a = float(x)
#         b = int(a)
#     except (TypeError, ValueError):
#         pass
#     else:
#         return b
#     try:
#         a = float(x)
#     except (TypeError, ValueError):
#         return x
#     else:
#         return float(x)


# def csv_read(filename):
#     f = open(filename, 'r')
#     # f = open(r'./etc/data/auto93.csv', 'r')

#     reader = csv.reader(f)
#     t = []
#     for row in reader:
#         t.append([typecheck(ele) for ele in row])
#     # if fun is not None:
#     #     fun(t)
#     return t

# def cosine(a, b, c):
#     den = 1 if c == 0 else 2 * c
#     x1 = (a**2 + c**2 - b**2) / den
#     x2 = max(0, min(1, x1))
#     y = abs((a**2 - x2**2)) ** 0.5
#     return x2, y

# def last(t):
#     if type(t) == dict:
#         x = list(t.values())[-1]
#     else:
#         x = t[-1] 
#     return x


# def show(node, what=None, cols=None, n_places=None, lvl=None):
#     if node:
#       lvl = lvl or 0
#       print("|.. " * lvl, end="")
#       if ("left" not in node):
#           print(last(last(node["data"].rows).cells))
#       else:
#           print(str(int(100 * node["C"])))
#       show(node.get("left", None), what, cols, n_places, lvl+1)
#       show(node.get("right", None), what, cols, n_places, lvl+1)

# def copy(t):
#     if isinstance(t, list) or isinstance(t, dict):
#         return deepcopy(t)

# def repRows(t, rows):
#     rows = copy(rows)
#     for j,s in enumerate(rows[len(rows)-1]):
#         rows[0][j] = str(rows[0][j]) + ' : ' + str(s)
#     rows.pop()
#     for n,row in enumerate(rows):
#         if n==0:
#             row.append('thingX')
#         else:
#             u = t.get('rows')[len(t.get('rows')) -n]
#             row.append(u[len(u)-1])
#     return data.DATA(rows)

# def any(t):
#     rintVal = rint1(None, len(t)-1)
#     return t[rintVal]

# def rint1(lo, hi):
#             return math.floor(0.5 + rand(lo, hi))

# def repPlace(data):
#   n,g = 20,[]
#   for i in range(n+1):
#       g.append([])
#       for j in range(n+1):
#           g[i].append(" ")
#   maxy = 0
#   print("")
#   for r, row in enumerate(data.rows):
#       c = chr(r+65)
#       print(c, last(row.cells))
#       x, y = int(row.x*n), int(row.y*n)
#       maxy = max(maxy, y)
#       g[y][x] = c
#   print("")
#   for y in range(maxy):
#       print("{" + "".join(g[y]) + "}")

# def repgrid(sFile, t, rows, cols):
#   t = exec(open(sFile).read())
#   rows = repRows(t, transpose(t["cols"]))
#   cols = repCols(t["cols"])
#   show(rows.cluster())
#   show(cols.cluster())
#   repPlace(rows)

# def transpose(t):
#     u = []
#     for i in range(len(t[0])):
#         u.append([t[j][i] for j in range(len(t))])
#     return u

# def dofile(fileName):
#     with open(fileName) as f:
#         return json.load(f)

# def repCols(cols):
#     copycols = deepcopy(cols)
#     for  col in cols:
#         col[-1] = str(col[0]) + ":" + str(col[-1])
#         for j in range(1, len(col)):
#             col[j-1] = col[j]
#         col.pop()
#     cols.insert(0, ['Num' + str(k) for k in range(len(cols[0]))])   
#     cols[0][-1] = "thingX"
#     # cols = {k:{j:l for j,l in enumerate(v)} for k,v in enumerate(cols)}
#     return data.DATA(cols)

# def any(t):
#     rintVal = rint(None, len(t)-1)
#     return t[rintVal]

# def rint(lo, hi):
#             return math.floor(0.5 + rand(lo, hi))


