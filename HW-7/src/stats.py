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

def scottKnot(rxs):
  def merges(i,j):
    out = functions.RX([],rxs[i]['name'])
    for k in range(i, j+1):
        out = functions.merge(out, rxs[j])
    return out
  
  def same(lo,cut,hi):
    l= merges(lo,cut)
    r= merges(cut+1,hi)
    return functions.cliffsDelta(l['has'], r['has']) and bootstrap(l['has'], r['has'])
  
  def rxs_sort(rxs):
    for i, x in enumerate(rxs):
        for j, y in enumerate(rxs):
            if functions.mid(x) < functions.mid(y):
                rxs[j], rxs[i] = rxs[i], rxs[j]
    return rxs
    
  def recurse(lo,hi,rank):
    b4 = merges(lo,hi)
    best = 0
    cut = None
    for j in range(lo,hi+1):
      if j < hi:
        l   = merges(lo,  j)
        r   = merges(j+1, hi)
        now = (l['n']*(functions.mid(l) - functions.mid(b4))**2 + r['n']*(functions.mid(r) - functions.mid(b4))**2) / (l['n'] + r['n'])
        if now > best:
          if abs(functions.mid(l) - functions.mid(r)) >= cohen:
            cut, best = j, now
    if cut != None and not same(lo, cut, hi):
      rank = recurse(lo, cut, rank) + 1
      rank = recurse(cut+1, hi,  rank) 
    else:
      for i in range(lo, hi+1):
        rxs[i]['rank'] = rank
    return rank
  rxs = rxs_sort(rxs)
  cohen = functions.div(merges(0,len(rxs)-1)) * 0.35
  recurse(0, len(rxs)-1, 1)
  return rxs

def tiles(rxs):
  huge = float('inf')
  lo,hi = huge, float('-inf')
  for rx in rxs: 
    lo,hi = min(lo,rx['has'][0]), max(hi, rx['has'][len(rx['has'])-1])
  for rx in rxs:
    t,u = rx['has'],[]
    def of(x,most):
        return int(max(1, min(most, x)))
    
    def at(x):
        return t[of(len(t)*x//1, len(t))]

    def pos(x):
        return math.floor(of(40*(x-lo)/(hi-lo+1E-32)//1, 40))

    for i in range(41):
        u.append(" ")
    a,b,c,d,e= at(.1), at(.3), at(.5), at(.7), at(.9) 
    A,B,C,D,E= pos(a), pos(b), pos(c), pos(d), pos(e)
    for i in range(A,B+1):
        u[i]="-"
    for i in range(D,E+1):
        u[i]="-"
    u[40//2] = "|" 
    u[C] = "*"
    form = "%6.2f"
    rx["show"] = rx["show"] + ''.join(u) + "{" + form % a
    for x in [b, c, d, e]:
        rx["show"]= rx["show"] + ", " + form % x
    rx["show"] = rx["show"] + "}"
  return rxs