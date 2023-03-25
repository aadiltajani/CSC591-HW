import sys
import math
import random
sys.path.append("./HW-7/src")

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

