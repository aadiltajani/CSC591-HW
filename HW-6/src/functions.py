import json
import math
import csv
import re
import sys
from copy import deepcopy
import data
import NUM
import SYM
import row
import col
import data
sys.path.append("./HW-6/src")


def rule(ranges, maxSize):
    t = {}
    for _,range in ranges:
        t['range']['txt'] = t['range']['txt'] or {}
        t['range']['txt'].append({'lo':range['lo'],'hi':range['hi'],'at':range['at']})
        return prune(t,maxSize)

def prune(rule, maxSize):
    n=0
    for txt,ranges in enumerate(ranges):
        n = n+1
        if len(ranges) == maxSize[txt]:
            n = n-1
            rule[txt] = None
    if n > 0:
        return rule


def Range(at,txt,lo,hi = None):
    if hi is None:
        hi = lo
    y = SYM.SYM()
    return {'at': at, 'txt': txt, 'lo': lo, 'hi': hi, 'y': y}

def rint(lo, hi, Seed =  93716211):
            return math.floor(0.5 + rand(lo, hi, Seed))

def rand(lo=0, hi=1, Seed =  93716211):
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi - lo) * Seed / 2147483647

def coerce(s: str):
    def fun(s1: str):
        if s1 == 'true' or s1.lower() == 'true':
            return True
        if s1 == 'false' or s1.lower() == 'false':
            return False
        return s1
    val = s
    try:
        val = float(s)
        if val == int(val):
            val = int(val)
    except ValueError:
        val = fun(re.search('^\s*(.+?)\s*$', s).group(1))
    return val

# def add(col,x, n=1):
#     if x != "?":
#         col['n'] = col['n'] + n
#         if col['isSym']:
#             col['has'][x] = n + (col['has'][x] if x in col['has'].keys() else 0)
#             if col['has'][x] > col['most']:
#                 col['most'], col['mode'] = col['has'][x],x
#         else:
#             col['lo'], col['hi'] = min(x,col['lo']), max(x,col['hi'])
#             all = len(col['has'])
#             pos = (all < 512 and all+1) or (rand() < 512/col['n'] and rint(1,all))
#             if pos:
#                 col['has'][pos] = x
#                 col['ok'] = False

def add(col,x,n):
    Is = {}
    def sym(t):
        t['x'] = n + (t['x'] or 0) 
        if t['x'] > col['most']:
            col['most'],col['mode'] = t['x'],x
    def num(t):
        col['lo'], col['hi'] = math.min(x,col['lo']), math.max(x,col['hi']) 
        if len(t) < Is['max']:
            col['ok']=False 
            t[len(t) + 1]=x
        elif rand() < Is['max']/col['n']:
            col['ok']=False
            t[rint(1, len(t))]=x
    if x!="?":
        n = n or 1
        col['n'] = col['n'] + n
        if col['isSym']:
            sym(col['has'])
        else:
            num(col['has'])

def itself(x):
    return x

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
        col['has'] = dict(sorted(col['has'].items()))
    col['ok'] = True
    return col['has']
    

def per(t, p=0.5):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(0, min(len(t), p - 1))] 

def mid(col):
    if col['isSym']:
        return col['mode']
    else:
        return per(has(col), .5)

def div(col):
    if col['isSym']:
        e=0
        for n in col['has'].values():
            e= e-n/col['n'] * math.log(n/col['n'],2)
        return e
    else:
        return (per(has(col),.9) - per(has(col), .1))/2.58

def stats(data, fun = None, places = 3,cols = None):
    cols= cols or data['cols']['y']
    def temp(k,col):
        return rnd(fun(col) if fun else mid(col), places), col['txt']

    tmp = kap(cols, temp)
    tmp['N'] = len(data['rows'])

    return tmp, map(cols, mid)

def norm(num,n):
    if n == '?':
        return n
    else:
        return (n - num['lo'])/(num['hi'] - num['lo'] + 1/float('inf'))

def value(has, nB=1, nR=1, sGoal=True):
    # print(has)
    # sGoal,nB,nR = sGoal or True, nB or 1, nR or 1
    b,r = 0,0
    for x,n in has.items():
        if x==sGoal:
            b = b + int(n) 
        else:
            r = r + int(n)
    b,r = b/(nB+1/float('inf')), r/(nR+1/float('inf'))
    return b**2/(b+r)

def kap(t, fun):
    u = {}
    for v in t:
        v, k = fun(t.index(v), v)
        if k in u.keys():
            u[k] = v
        else:
            u[len(u) + 1] = v
    return u
# Numerics
# Seed = 937162211


# def rint(lo, hi):
#   return math.floor(0.5 + rand(lo, hi))

# global Seed

def cliffsDelta(ns1, ns2):
    if len(ns1) > 256:
        ns1 = many(ns1, 256)
    if len(ns2) > 256:
        ns2 = many(ns2, 256)
    if len(ns1) > 10*len(ns2):
        ns1 = many(ns1, 10*len(ns2))
    if len(ns2) > 10*len(ns1):
        ns2 = many(ns2, 10*len(ns1))
    n, gt, lt = 0, 0, 0
    for x in ns1:
        for y in ns2:
            n += 1
            if x > y:
                gt += 1
            if x < y:
                lt += 1
    return abs(lt-gt)/n > 0.147

def rnd(n, places=3):
    mult = 10 ** places
    return math.floor(n * mult + 0.5) / mult


# # Lists
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


def dist(data, t1, t2, cols= None):
    def dist1(col, x, y):
        if x == '?' and y =='?':
            return 1
        if col['isSym']:
            return 0 if x == y else 1
        
        x, y = norm(col, x), norm(col, y)
        if x == "?":
            x = 1 if y < 0.5 else 1
        if y == "?":
            y = 1 if x < 0.5 else 1
        return abs(x - y)
    
    d, n = 0, 1/float('inf')

    cols = cols if cols else data['cols']['x']
    for col in cols:
        n += 1
        d += dist1(col, t1[col['at']], t2[col['at']])

    return (d / n)**(1 / 2)

def temp(k, nums, nums2, the):
    return cliffsDelta(nums.has, nums2[k].has, the), nums.txt

def diffs(nums1, nums2):
    def kap(nums1, func):
        return [func(k, nums) for k, nums in enumerate(nums1)]

    return kap(nums1, lambda k, nums: (cliffsDelta(nums["has"], nums2[k]["has"]), nums["txt"]))

def better(data, row1, row2):
    s1 = 0
    s2 = 0
    ys = data["cols"]["y"]
    for _, col in enumerate(ys):
        x = norm(col, row1[col['at']])
        y = norm(col, row2[col['at']])

        s1 = s1 - math.exp(col['w'] * (x-y)/len(ys))
        s2 = s2 - math.exp(col['w'] * (y - x)/len(ys))

    # if (len(ys) == 0):
    #     return s1 < s2
    return s1/len(ys) < s2 / len(ys)
def many(t, n):
    return [any(t) for i in range(n)]


def tree(d, r=None, cols=None, above=None):
    r = r if r else d['rows']
    here = {"data": data.clone(d, r)}
    if len(r)>=2*(len(d['rows'])**0.5):
        left, right, A, B, _ = half(d, r, cols, above)
        here['left'] = tree(d, left, cols, A)
        here['right'] = tree(d, right, cols, B)
    return here

def showTree(tree, lvl=0, post=None):
    if tree:
        print("{}[{}]".format("|.. " * lvl, len(tree["data"]["rows"])), end="")
        if not "left" in tree or lvl == 0:
            print(stats(tree["data"]))
        else:
            print("")

        showTree(tree.get('left'), lvl + 1)
        showTree(tree.get('right'), lvl + 1)

def half(data, rows = None, cols = None, above = None):
   
    def gap(r1, r2):
        return dist(data, r1, r2, cols)
    def cos(a, b, c):
        return (a**2 + c**2 - b**2)/(2*c +1)
    def proj(r):
        return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}
    rows = rows or data['rows']
    some = many(rows, 512)
    A = above or any(some)
    tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
    far = tmp[int(len(tmp)*0.95)]
    B, c = far["row"], far["d"]
    # print(far)
    sorted_rows = sorted(map(rows, proj).values(), key=lambda x: x["x"])
    left, right = [], []
    for n, two in enumerate(sorted_rows):
        if n <= (len(rows) - 1) / 2:
            left.append(two["row"])
        else:
            right.append(two["row"])
    return left, right, A, B, c

def sway(d):
    def worker(rows, worse, above=None):
        if len(rows) <= len(d["rows"])**0.5:
            return rows, many(worse, 4 * len(rows))
        else:
            l, r, A, B, dummy = half(d, rows, None, above)
            if better(d, B, A):
                l, r, A, B = r, l, B, A
            for row in r:
                worse.append(row)
            return worker(l, worse, A)

    best, rest = worker(d["rows"], [])
    return data.clone(d, best), data.clone(d, rest)


# def sort(t):
#     t = sorted(t)
#     return t


# def keys(t):
#     return sorted(t.keys())


# # Strings
def oo(t):
    print(o(t))
    return True


# def fmt(s, *a):
#     return str.format(s, a)


def o(t):
    if isinstance(t, dict):
        return t
    
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

def any(t):
    return t[rint(0, len(t) - 1)]

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




