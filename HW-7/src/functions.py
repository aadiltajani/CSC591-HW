import json
import math
import csv
import re
import sys
from copy import deepcopy
import data
import NUM
import row
import data
sys.path.append("./HW-7/src")




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

def mid(col):
    pass

def div(col):
    pass



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


# # Strings
def oo(t):
    print(o(t))
    return True

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

def any(t):
    return t[rint(0, len(t) - 1)]
