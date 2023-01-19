import sys
sys.path.append("./src")
from functions import *
from NUM import NUM


egs = {}
the = {}
def eg(k, s, fun):
    egs[k] = fun

def numTest1():
    num1 = NUM()
    num2 = NUM()
    global Seed
    Seed = the['seed']

    for i in range(1, 10**3):
        num1.add(rand(0, 1))
    for i in range(1, 10**3):
        num2.add(rand(0, 1))
        
    m1, m2 = rnd(num1.mid(),10), rnd(num1.mid(),10)

    return m1==m2 and .5 == rnd(m1, 1)

def numTest2():
    num = NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())

eg("the","show settings",oo(the))
eg("rand","generate, reset, regenerate same",numTest1)
eg("num", "check nums", numTest2)

print(egs)