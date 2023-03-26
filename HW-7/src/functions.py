import math
import sys
import stats
sys.path.append("./HW-7/src")

def RX(t, s = ""):
    return {"name":s, "rank":0, "n":len(t), "show":"", "has":sorted(t)}

def mid(t):
    t= t['has'] if t['has'] else t
    n = (len(t)-1)//2
    return (t[n] +t[n+1])/2 if len(t)%2==0 else t[n+1]

def div(t):
    t= t['has'] if t['has'] else t
    return (t[ len(t)*9//10 ] - t[ len(t)*1//10 ])/2.56

def merge(rx1, rx2):
    rx3 = RX([], rx1['name'])
    rx3['has'] = rx1['has'] + rx2['has']
    rx3['has'] = sorted(rx3['has'])
    rx3['n'] = len(rx3['has'])
    return rx3

def cliffsDelta(ns1, ns2): 
    n, gt, lt = 0, 0, 0 
    if len(ns1) > 128: 
        ns1 = stats.samples(ns1, 128)
    if len(ns2) > 128: 
        ns2 = stats.samples(ns2, 128)
    for x in ns1:
        for y in ns2: 
            n = n + 1 
            if x > y: 
                gt += 1
            if x < y: 
                lt += 1
    return abs(lt - gt) / n <= 0.4

def add(i, x):
    i['n'] += 1
    d = x - i['mu']
    i['mu'] = i['mu'] + d / i['n']
    i['m2'] = i['m2'] + d * (x - i['mu'])
    i['sd'] = 0 if i['n'] < 2 else (i['m2'] / (i['n'] - 1)) ** 0.5

def num(t = []):
    i = {'n':0, 'mu':0, 'm2':0, 'sd':0}
    if len(t) > 0:
        for x in t:
            add(i, x)
    return i