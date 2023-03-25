import sys
import math
import random
import functions
sys.path.append("./HW-7/src")

random.seed(1)

def erf(x, a1, a2, a3, a4, a5, p, sign): 
    a1, a2, a3, a4, a5, p = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429, 0.3275911
    sign = 1 
    if x < 0: 
        sign = -1 
    x = math.abs(x)
    t = 1.0 / (1.0 + p*x)
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1) * t * math.exp(-x * x)
    return sign * y 

def gaussian(mu = 0, sd = 1): 
    return  mu + sd * math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random())

def samples(t, n = None): 
    u = []
    for i in range(n if n is not None else len(t)): 
        u.append(random.choice(t))
    return u

def delta(i, other): 
    e, y, z = 1E-32, i, other
    return abs(y['mu'] - z['mu']) / (e + y['sd'] ** 2 / y['n'] + z['sd'] **2 / z['n']) ** 0.5 

def bootstrap(y0, z0): 
    x, y, z, yhat, zhat = functions.num(), functions.num(), functions.num(), [], []
    for y1 in y0:
        functions.add(x, y1)
        functions.add(y, y1)
    for z1 in z0:
        functions.add(x, z1)
        functions.add(z, z1)
    xmu, ymu, zmu = x['mu'], y['mu'], z['mu']
    for y1 in y0: 
        yhat.append(y1 - ymu + xmu)
    for z1 in z0: 
        zhat.append(z1 - zmu + xmu)
    tobs = delta(y, z)
    n = 0
    for i in range(512):
        if delta(functions.num(samples(yhat)), functions.num(samples(zhat))) > tobs:
            n += 1
    return n / 512 >= 0.05

def scottKnot():
    pass

def tiles():
    pass